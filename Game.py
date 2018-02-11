from math import *
import pygame,os
from entities import *
from globalvars import *

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


if __name__ == '__main__':

    os.environ["SDL_VIDEO_CENTERED"] = "1" #center the window to the center of the screen.
    pygame.init()
    running = True

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("game")
    background = Background(os.path.join("resources","Background.png"),(0,0))

    clock = pygame.time.Clock()
    player = Player()
    testenemy = Enemy(start_pos=(100,100), size=(1,1))

    enemies.append(testenemy)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while running:

        clock.tick(60)
        screen.fill(white)
        screen.blit(background.image,background.rect)
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

        player.move(pygame.key.get_pressed())
        if pygame.key.get_pressed()[pygame.K_z]:
            if player.shoot_timer:
                player.shoot_timer -= 1
            else:
                player.shoot(player.box.center, bullets)
                player.shoot_timer = 60/6


        # movement of other entities
        for bullet in bullets:
            all_sprites.add(bullet)
            bullet.move()

        for enemy in enemies:
            enemy.move()
        
        #draw
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
