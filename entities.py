import pygame
from globalvars import *
class Player(object):
    def __init__(self, **kwargs):
        self.box = pygame.Rect(width/2, height/2, kwargs.get("width",50), kwargs.get("height",50))

    def move(self, dx, dy):
        if dx != 0 or dy != 0:
            self.move_xy(dx, dy)

    def move_xy(self, dx, dy):
        self.box.move_ip(dx,0)
        self.box.move_ip(0,dy)

class Enemy(object):
    def __init__(self, **kwargs):
        self.box = pygame.Rect(width/2,height/2,)
