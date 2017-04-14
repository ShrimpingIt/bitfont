from PIL import Image,ImageDraw
from os import chdir,path
import string,re

white = "white"
black = "black"

def normalise_color(color):
    if color == white:
        color = 1
    elif color == black:
        color = 0
    assert color == 0 or color == 1, "Unrecognised color specification"
    return color

class BitScreen():

    def __init__(self, width=128,height=64, imageType="1", color=white):
        color = normalise_color(color)
        self.image = Image.new(imageType, (width, height), color=color)
        self.pixelMap = self.image.load()

    def create_plotter(self, color=black):
        color = normalise_color(color)
        def plot(x,y):
            self.pixelMap[x,y] = color
        return plot

def strip_space(text):
    return "\n".join([line.strip() for line in text.split('\n')])

def run():
    from faces.font_5x7 import font
    message = strip_space(
            """You are an officer at the
            coastal fort at Senhouse.
            You must watch the coast
            for attack from the sea!"""
    )
    (width, height) = font.para_dims(message)
    screen = BitScreen(width=width, height=height)
    plotter = screen.create_plotter()
    font.draw_para(message, 0, 0, plotter, font.height)
    chdir(path.dirname(__file__))
    screen.image.save("pillow.png")

if __name__ == "__main__":
    run()