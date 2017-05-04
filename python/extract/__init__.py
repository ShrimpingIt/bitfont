from PIL import Image, ImageFont, ImageDraw
import os
import bitfont

'''The sequence of printable ascii character'''
asciiSequence = ''.join([chr(x) for x in range(bitfont.asciiFirst, bitfont.asciiEnd)])

'''Aliases for character names needing special treatment in shell/filesystem'''
charAliases = {"?": "QUESTION", "!": "EXCLAMATION", ".": "STOP", "/": "FWDSLASH", "\\": "BACKSLASH", "`": "BACKTICK"}

'''
The pilfont utility allows BDF files to be exported to .pil format supported by Python Imaging Library
.bdf files were exported to PIL-compatible font .pil files, with their associated .pbm glyph data like...

(see http://effbot.org/imagingbook/imagefont.htm). This function renders .pil files to pngs for inspection
'''
def font_to_sample(pilPath):
    fontPrefix, extensionSuffix = os.path.splitext(os.path.basename(pilPath))
    font = ImageFont.load(pilPath)
    # calculate tile one pixel bigger than text
    textSize = font.getsize(asciiSequence)
    image = Image.new("RGBA", textSize, "black")
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), asciiSequence, font=font)
    imagePath = os.path.join("rendered", fontPrefix + ".png")
    try:
        image.save(imagePath)
    except:
        pass

def font_to_sample_chars(pilPath):
    font = ImageFont.load(pilPath)
    fontPrefix, extensionSuffix = os.path.splitext(os.path.basename(pilPath))
    renderedDir = os.path.join("rendered", fontPrefix)
    os.makedirs(renderedDir, exist_ok=True)
    for entry in asciiSequence:
        imageSize = font.getsize(entry)
        if 0 not in imageSize: # check the character has extent
            image = Image.new("RGBA", imageSize, "black")
            draw = ImageDraw.Draw(image)
            draw.text((0,0), entry, font=font)
            entryPrefix = entry
            if entryPrefix in charAliases:
                entryPrefix = charAliases[entryPrefix]
            imagePath = os.path.join(renderedDir, entryPrefix + ".png")
            image.save(imagePath)

def pilfont_to_bitfont(pilPath, stripBlankCols=False):
    font = ImageFont.load(pilPath)
    fontPrefix, extensionSuffix = os.path.splitext(os.path.basename(pilPath))
    pixBytes = bytearray()
    endCols = list()
    fontHeight = None
    nextByte = 0
    nextBit = 0
    white = (255, 255, 255)
    for entry in asciiSequence:
        try:
            entrySize = font.getsize(entry)
            assert 0 not in entrySize, "Character has no extent"  # check the character has extent

            entryWidth, entryHeight = entrySize
            if fontHeight == None:
                fontHeight = entryHeight
            else:
                assert fontHeight == entryHeight, "Font has characters with varying heights"

            image = Image.new("RGB", entrySize, "black")
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), entry, font=font)
            pixels = image.load()

            # CH to optimise left/right bounding routines below, avoid list creation through comprehension over pixels

            if stripBlankCols:
                # crop any empty columns before and after
                for firstCol in range(entryWidth):
                    firstColPixels = [pixels[firstCol, y] for y in range(entryHeight)]
                    if white in firstColPixels:
                        break
                else:
                    # only space should have no black pixels
                    firstCol = 0
                    assert entry == " ", "Character has no set pixels, but is not a space"

                for lastCol in reversed(range(entryWidth)):
                    lastColPixels = [pixels[lastCol, y] for y in range(entryHeight)]
                    if white in lastColPixels:
                        break
                else:
                    # only space should have no black pixels
                    lastCol = entryWidth - 1
                    assert entry == " ", "Character has no set pixels, but is not a space"
            else:
                firstCol = 0
                lastCol = entryWidth - 1

            # store the non-empty columns into pixBytes, recording offsets
            for col in range(firstCol, lastCol + 1): # first to last inclusive
                for row in range(entryHeight):
                    if pixels[col, row] == white: # set the bit
                        nextByte = nextByte | 1 << (nextBit % 8)
                    nextBit += 1
                    if nextBit % 8 == 0:
                        pixBytes.append(nextByte)
                        nextByte = 0

            endCols.append(nextBit//fontHeight)

        except Exception as e:
            raise e

    # record partial byte if left over from ascii traversal
    if not (nextBit % 8 == 0):
        pixBytes.append(nextByte)

    return bitfont.BitFont(fontHeight, pixBytes, endCols)