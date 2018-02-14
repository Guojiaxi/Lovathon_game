from math import *
import pygame,os
import random
from entities import *
from globalvars import *

def wait():
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

def spawn():
    all_sprites.add(Enemy(start_pos=(random.randint(0, width), random.randint(0, 2 * height // 3))))

if __name__ == '__main__':

    os.environ["SDL_VIDEO_CENTERED"] = "1" #center the window to the center of the screen.
    pygame.init()
    running = True
    font = pygame.font.SysFont("Times New Roman",35)

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("game")
    background = Background(os.path.join("resources","Bloodinmyheart.png"),(0,0))

    screen.blit(background.image, background.rect)
    pygame.display.update()
    wait()

    background = Background(os.path.join("resources","Background.png"),(0,0))

    player = Player()

    all_sprites.add(player)

    while running:

        clock.tick(FPS)
        screen.fill(white)
        screen.blit(background.image,background.rect)
        player.is_hit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # basic movement

        if (pygame.key.get_pressed()[pygame.K_5]):
            all_sprites.add(Enemy(start_pos=(random.randint(0,width),random.randint(0,2*height//3))))
            
        scoreDisplay = font.render(str(player.score), 1, white)
        screen.blit(scoreDisplay,(0,0))

        player.move(pygame.key.get_pressed())

        if pygame.key.get_pressed()[pygame.K_z]:
            player.shoot(player.rect.center, bullets)
        else:
            player.shoot_timer = 0

        # movement of other entities
        for bullet in bullets:
            all_sprites.add(bullet)
            bullet.move()

        for enemy in enemies:
            enemy.move()
            enemy.is_hit(player)

        for enemy in enemies:
            if enemy.shoot_timer:
                enemy.shoot_timer -= 1
            else:
                enemy.shoot(enemy.rect.center, player.rect.center)
                enemy.shoot_timer = 120/1


        #draw
        if player.dead:
            background = Background(os.path.join("resources","GAMEOVER.png"),(0,0))
            screen.blit(background.image, background.rect)
            pygame.display.update()
            wait()
            player.image = pygame.image.load(os.path.join("resources","GOLD.png")).convert_alpha()
            background = Background(os.path.join("resources","Background.png"),(0,0))

            player.dead = False
            
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
