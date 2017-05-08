import pyglet
from pyglet.gl import *

# assists with scaling textures in expected (blocky) way, following https://gamedev.stackexchange.com/questions/20297/how-can-i-resize-pixel-art-in-pyglet-without-making-it-blurry
glEnable(GL_TEXTURE_2D)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

from faces.font_5x7 import font

class BitScreen():

    def __init__(self):
        self.window = pyglet.window.Window(width=1024,height=512)

        def plotter(x, y):
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                                 ('v2i', (x, self.window.height - y))
                                 )

        @self.window.event
        def on_draw():
            self.window.clear()
            font.draw_line("Hello World", plotter, 1, 1)

    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    screen = BitScreen()
    screen.run()
