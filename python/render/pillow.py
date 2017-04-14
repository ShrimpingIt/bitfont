from PIL import Image,ImageDraw
from os import chdir,path
import string,re

class BitScreen():

    def __init__(self, width=128,height=64, imageType="1", color=1):
        self.image = Image.new(imageType, (width, height), color=color)
        self.pixelMap = self.image.load()
        self.white = False
        def plot(x,y):
            self.pixelMap[x,y] = 1 if self.white else 0
        self.plot = plot

def strip_space(text):
    return "\n".join([line.strip() for line in text.split('\n')])

def run():
    from faces.font_5x7 import font
    #message = string.ascii_letters
    message = strip_space(
            """You are an officer at the
            coastal fort at Senhosue.
            You must watch the coast
            for attack from the sea!"""
    )
    (width, height) = font.para_dims(message)
    screen = BitScreen(width=width, height=height)
    font.draw_para(message, 0, 0, screen.plot, font.height - 1)
    chdir(path.dirname(__file__))
    screen.image.save("pillow.png")

if __name__ == "__main__":
    run()