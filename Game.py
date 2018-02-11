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
    testenemy = Enemy(start_pos=(100,100), size=(1,1))

    enemies.append(testenemy)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while running:

        clock.tick(60)
        screen.fill(white)
        pygame.draw.rect(screen,black,[0,0,10,10])
        #print(bullets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # basic movement
        key = pygame.key.get_pressed()
        if (key[pygame.K_5]):
            all_sprites.add(testenemy)
        player.move(key)
        player.shoot(len(bullets),key,player.rect.center,bullets)

        # movement of other entities
        for bullet in bullets:
            all_sprites.add(bullet)
            bullet.move()
        #draw

        all_sprites.draw(screen)
        pygame.display.flip()



    pygame.quit()
