from math import *
import pygame,os
from entities import *
from globalvars import *


if __name__ == '__main__':
    os.environ["SDL_VIDEO_CENTERED"] = "1" #center the window to the center of the screen.
    pygame.init()
    running = True

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("game")


    clock = pygame.time.Clock()
    player = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while running:

        clock.tick(50)
        screen.fill(white)
        all_sprites.draw(screen)
        #print(bullets)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # basic movement
        key = pygame.key.get_pressed()

        player.move(key)

        if key[pygame.K_z]:
            player.shoot(len(bullets),key,player.box.center,bullets)

        # movement of other entities
        for bullet in bullets:
            all_sprites.add(bullet)
            bullet.move()

        #draw
        pygame.display.flip()



    pygame.quit()
