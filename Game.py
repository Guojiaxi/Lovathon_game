from math import *
import pygame, os

class Player(object):
    def __init__(self):
        self.box = pygame.Rect(width/2, height/2, 50, 50)

    def move(self, dx, dy):
        if dx != 0 or dy != 0:
            self.move_xy(dx, dy)

    def move_xy(self, dx, dy):
        self.box.move_ip(dx,0)
        self.box.move_ip(0,dy)




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

speed = 5

while running:

    clock.tick(60)

    screen.fill(white)
    pygame.draw.rect(screen, black, player.box, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # basic movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if player.box.left >= 0:
            player.move(-speed,0)

    if key[pygame.K_RIGHT]:
        if player.box.right <= width:
            player.move(speed,0)

    if key[pygame.K_UP]:
        if player.box.top >= 0:
            player.move(0,-speed)

    if key[pygame.K_DOWN]:
        if player.box.bottom <= height:
            player.move(0,speed)

    #draw
    pygame.display.flip()



pygame.quit()
