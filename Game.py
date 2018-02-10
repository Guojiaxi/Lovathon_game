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

while running:

    clock.tick(60)
    screen.fillplayer.move(white)
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
