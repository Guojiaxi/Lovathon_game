from math import *
import pygame, os

class Bullet(object):
    def __init__(self,**kwargs):
        pass



class Player(object):
    def __init__(self):
        self.box = pygame.Rect(width/2, height/2, 50, 50)
        self.speed = 6

    def move(self,key):
        if key[pygame.K_LSHIFT]:
            self.speed = 3
        else:
            self.speed = 6

        if key[pygame.K_LEFT]:
            if self.box.left >= 0:
                self.move_xy(-self.speed, 0)

        if key[pygame.K_RIGHT]:
            if self.box.right <= width:
                self.move_xy(self.speed, 0)

        if key[pygame.K_UP]:
            if self.box.top >= 0:
                self.move_xy(0, -self.speed)

        if key[pygame.K_DOWN]:
            if self.box.bottom <= height:
                self.move_xy(0, self.speed)

    def move_xy(self, dx, dy):
        if dx != 0 or dy != 0:
            self.box.move_ip(dx, 0)
            self.box.move_ip(0, dy)




os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
running = True

width = 800
height = 608
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("game")

white = (255,255,255) #RGB
black = (0,0,0)

clock = pygame.time.Clock()
player = Player()

while running:

    clock.tick(60)

    screen.fill(white)
    pygame.draw.rect(screen, black, player.box, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # basic movement
    key = pygame.key.get_pressed()
    player.move(key)

    #draw
    pygame.display.flip()



pygame.quit()
