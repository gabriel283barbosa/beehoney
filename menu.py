import pygame
from obj import Obj

class Menu:
    def __init__(self,image):

        self.bg = Obj(image, 0 , 0)

        self.cenas = False

    def draw(self,window):
        self.bg.group.draw(window)

    def events(self,events):
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RETURN:
                self.cenas = True

class GamerOver(Menu):
    def __init__(self, image):
        super().__init__(image)