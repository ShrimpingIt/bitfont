from PIL import Image,ImageDraw
from os import chdir,path

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

def run():
    from faces.font_5x7 import font
    message = """Pretend to CARRY the
heavy bucket back to
the main building
Don't spill any"""
    (width, height) = [dim for dim in font.para_dims(message)]
    screen = BitScreen(width=width, height=height)
    plotter = screen.create_plotter()
    font.draw_para(message, plotter, 0, 0, font.height )
    chdir(path.dirname(__file__))
    screen.image.save("pillow.png")

if __name__ == "__main__":
    run()
