from math import *
import pygame, os
from entities import *
from globalvars import *

os.environ["SDL_VIDEO_CENTERED"] = "1" #center the window to the center of the screen.
pygame.init()
running = True

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("game")

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
