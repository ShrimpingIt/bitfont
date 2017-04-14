import os
from os import path, chdir
import glob
import extract

chdir(path.dirname(__file__))
# get all pil pixel font files in the current directory
pilPaths = glob.glob("*.pil")
pilPaths.sort()
pilPaths = [path.realpath(pilPath) for pilPath in pilPaths]  # make pilPaths absolute
facesDir = "../faces"
os.makedirs(facesDir, exist_ok=True)
chdir(facesDir)
for pilPath in pilPaths:
    fontPrefix, extensionSuffix = os.path.splitext(os.path.basename(pilPath))
    try:
        font = extract.pilfont_to_bitfont(pilPath)
        fontPath = os.path.realpath("font_" + fontPrefix + ".py")
        with open(fontPath, "w") as f:
            f.write("from bitfont import BitFont\n")
            f.write("font = BitFont(\n")
            f.write("\t" + ",\n\t".join([
                "height = " + str(font.height),
                "pixBytes = " + str(font.pixBytes),
                "endCols = " + str(font.endCols),
            ]))
            f.write("\n)")
    except AssertionError as ae:
        message = ae.args[0]
        if "no set pixels" in message or "no extent" in message:
            print("Couldn't process " + fontPrefix + " : " + message)
            pass
        else:
            raise ae