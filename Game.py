from math import *
import pygame, os

class Wall:
    def __init__(self, pos, width, height):
        walls.append(self)
        self.box = pygame.Rect(pos[0],pos[1],width,height)

class Player(object):
    def __init__(self):
        self.hitbox = pygame.Rect(24+width/2, 24+height/2, 5, 5)
        self.box = pygame.Rect(width/2, height/2, 51, 51)

    def move(self, dx, dy):
        if dx != 0 or dy != 0:
            self.move_xy(dx, dy)

    def move_xy(self, dx, dy):
        self.hitbox.move_ip(dx,0)
        self.hitbox.move_ip(0,dy)

        for wall in walls: # COLLISION DETECTION
            if self.hitbox.colliderect(wall.box):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.box.right = wall.box.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.box.left = wall.box.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.box.bottom = wall.box.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.box.top = wall.box.bottom

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
running = True

while running:
    pass
