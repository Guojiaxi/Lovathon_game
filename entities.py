import pygame,os
from globalvars import *
from Game import *

class Player(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        super().__init__()
        self.image = pygame.image.load(os.path.join("resources","GOLD.png")).convert_alpha()
        pygame.draw.rect(self.image,white,[1,1,1,1])
        self.rect = self.image.get_rect()
        self.box = self.rect

        print(self.rect.left,self.rect.right)
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

    def shoot(self,index,key,current_position,bullets):
        bullets.append(PlayerBullet(index,start_pos=(current_position[0]-3,current_position[1]-30), speed=15))

class Enemy(object):
    def __init__(self, **kwargs):
        self.box = pygame.Rect(kwargs.get("start_pos",(width/2,0)),kwargs.get("size",(50,50)))
        enemies.append

  
class Bullet(pygame.sprite.Sprite):
    def __init__(self,**kwargs):
        super().__init__()
        self.hitbox = pygame.Rect(kwargs.get("start_pos",(0,0)),kwargs.get("size",(10,10)))

        self.speed = kwargs.get("speed",7)

class PlayerBullet(Bullet):
    def __init__(self,index,**kwargs):
        Bullet.__init__(self,**kwargs)
        self.index = index
        self.image = pygame.image.load(os.path.join("resources","GoodBullet.png")).convert_alpha()
        pygame.draw.rect(self.image,white,self.hitbox)
        self.rect = self.image.get_rect()


    def move(self):
        if self.rect.bottom >= 0:
            self.rect.move_ip(0,-self.speed)
        else:
            bullets.remove(self)

class EnemyBullet(Bullet):
    def __init__(self):
        super(Bullet,self).__init__()
