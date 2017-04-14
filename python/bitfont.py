firstAsciiChar = 32
endAsciiChar = 127

class BitFont():
    """A BitFont provides logic for plotting pixels from a fixed-height font, using columns of bits indexed from a bytearray"""

    def __init__(self, height, pixBytes, endCols):
        """Initialise a bitfont
        :param height: number of pixels in each column of the bitFont
        :param pixBytes: the bits for each column in ascii, left to right order
        :param endCols: the column following each ascii character
        """
        self.height = height
        self.pixBytes = pixBytes
        self.endCols = endCols

    def col_bounds(self, ascii):
        """Return the range of columns used by a character
        :param ascii: the character as an ascii byte
        :return: (firstCol, endCol) the character starts at firstCol and ends before endCol
        """
        assert ascii < endAsciiChar
        # remap from ascii to endOffsets lookup
        endIndex = ascii - firstAsciiChar
        # start, end bits defined by previous,current character
        firstCol = self.endCols[endIndex - 1] if endIndex > 0 else 0
        endCol = self.endCols[endIndex]
        return (firstCol, endCol)

    def bit_bounds(self, ascii):
        """Return range of bit indexes used by a character
        :param ascii: the character as an ascii byte
        :return: (firstBit, endBit) the character starts at firstBit and ends before endBit
        """
        cols = self.col_bounds(ascii)
        return (cols[0] * self.height, cols[1] * self.height)

    def byte_cols(self, ascii):
        """Return number of columns in a character
        :param ascii: the character as an ascii byte
        :return:
        """
        cols = self.col_bounds(ascii)
        return cols[1] - cols[0]

    def line_cols(self, line):
        """Return number of columns in a line of text
        :param ascii: the character as an ascii byte
        :return:
        """
        cols = 0
        for char in line:
            cols += self.byte_cols(ord(char))
        return cols

    def para_dims(self, para):
        lines = para.split("\n")
        maxX = 0
        for line in lines:
            lineX = self.line_cols(line)
            maxX = max(lineX, maxX)
        return (maxX, len(lines) * self.height)

    def draw_byte(self, ascii, x, y, plotter):
        """ Plot the points making up a character
        :param ascii: the character as a ascii byte
        :param x: x coord of top left pixel
        :param y: y coord of top left pixel
        :param plotter: a function which will be called as plotter(x,y) for every character bit
        :return: the number of pixel columns used by the character
        """
        assert ascii >= firstAsciiChar and ascii < endAsciiChar
        firstBit,endBit = self.bit_bounds(ascii)
        # read individual bits from pixBytes, and plot them
        drawBit = firstBit
        dX = 0
        dY = 0
        while drawBit != endBit:
            try:
                # byte index=integer division, bit index=remainder from integer division
                sourceByte = self.pixBytes[drawBit // 8]
                selectedBit = 1 << (drawBit % 8)
                # plot a point if the drawBit is set
                if not(sourceByte & selectedBit == 0):
                    plotter(x + dX, y + dY)
                drawBit += 1
                dY += 1
                # start new column if it's the last bit
                if (drawBit - firstBit) % self.height == 0:
                    dY = 0
                    dX += 1
            except IndexError as e:
                raise e
        return dX

    def draw_text(self, text, x, y, plotter):
        """Plot a single line of characters
        :param text: the characters as a string
        :param x: x coord of top left pixel
        :param y: y coord of top left pixel
        :param plotter: a function which will be called as plotter(x,y) for every character bit
        :return: the number of pixel columns used by the string
        """
        assert "\n" not in text
        dX = 0
        for char in text:
            dX += self.draw_byte(ord(char), x + dX, y, plotter)
        return dX

    def draw_para(self, para, x, y, plotter, lineHeight=None):
        if lineHeight == None:
            lineHeight = self.height
        """Plot multiple lines of characters
        :param para: the lines as a string
        :param x: x coord of top left pixel
        :param y: y coord of top left pixel
        :param plotter: a function which will be called as plotter(x,y) for every character bit
        :return: (cols, rows) total pixels used by the text drawn
        """
        lines = para.split("\n")
        maxX = 0
        dY = 0
        for line in lines:
            lineX = self.draw_text(line, x, y + dY, plotter)
            maxX = max(lineX, maxX)
            dY += lineHeight
        return (maxX, dY)