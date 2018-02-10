import pygame
from globalvars import *
class Player(object):
    def __init__(self, **kwargs):
        self.box = pygame.Rect(width/2, height/2, kwargs.get("width",50), kwargs.get("height",50))
        
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

    def shoot(self):

class Enemy(object):
    def __init__(self, **kwargs):
        self.box = pygame.Rect(width/2, height/2,)
  
class Bullet(object):
    def __init__(self,**kwargs):
        pass
        

class PlayerBullet(Bullet):
    def __init__(self):
        super(Bullet,self).__init__()

class EnemyBullet(Bullet):
    def __init__(self):
        super(Bullet,self).__init__()
