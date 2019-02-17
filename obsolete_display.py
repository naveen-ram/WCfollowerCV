import sys
import sdl2.ext
from time import sleep

class Display(object):
    def __init__(self, W, H):
        self.W = W
        self.H = H

    def create_window(self,imageUrl):
        sdl2.ext.init()
        window = sdl2.ext.Window("The Pong Game", size=(self.W, self.H))
        window.show()
        running = True
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
            window.refresh()

"""
    def createWindow():
        sdl2.ext.init()
        window = sdl2.ext.Window("The Pong Game", size=(self.W, self.H))
        window.show()
"""
