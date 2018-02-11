import pygame,os,random
from globalvars import *
from move_patterns import *


class Body(pygame.sprite.Sprite):
    def __init__(self,**kwargs):
        super().__init__()

        self.hitbox = pygame.Rect(kwargs.get("start_pos",(0,0)),kwargs.get("size",(1,1)))

class Player(Body):
    def __init__(self, **kwargs):
        Body.__init__(self,**kwargs)
        self.image = pygame.image.load(os.path.join("resources","GOLD.png")).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = (width / 2, height / 2)
        pygame.draw.rect(self.image,white,self.hitbox)
        self.shoot_timer = 60/6


    def move(self,key):
        if key[pygame.K_LSHIFT]:
            self.speed = 3
        else:
            self.speed = 6

        if key[pygame.K_LEFT]:
            if self.rect.left >= 0:
                self.move_xy(-self.speed, 0)

        if key[pygame.K_RIGHT]:
            if self.rect.right <= width:
                self.move_xy(self.speed, 0)

        if key[pygame.K_UP]:
            if self.rect.top >= 0:
                self.move_xy(0, -self.speed)

        if key[pygame.K_DOWN]:
            if self.rect.bottom <= height:
                self.move_xy(0, self.speed)

    def move_xy(self, dx, dy):
        if dx != 0 or dy != 0:
            self.rect.move_ip(dx, 0)
            self.rect.move_ip(0, dy)

    def shoot(self,current_position,bullets):
        bullets.append(PlayerBullet(start_pos=(current_position[0]-3,current_position[1]-30), speed=15))

    def is_hit(self):
        for thing in bullets:
            if thing is EnemyBullet and self.hitbox.colliderect(thing.hitbox):
                del bullets[bullets.index(thing)]
                # player needs to die or lose a life
                # explosion animation
        for enemy in enemies:
            if self.hitbox.colliderect(enemy.hitbox):
                # me ded
                pass

class Enemy(Body):
    def __init__(self, **kwargs):
        Body.__init__(self,**kwargs)
        self.image = pygame.image.load(os.path.join("resources", "BAD.png")).convert_alpha()
        pygame.draw.rect(self.image, white, self.hitbox)
        self.rect = self.image.get_rect()
        enemies.append(self)
        self.pattern = 1
        self.t = 0

    def move(self):
        (dx,dy) = move_pat[self.pattern](self.t)
        self.rect.move_ip(dx, 0)
        self.rect.move_ip(0, dy)
        self.t += 1


    def is_hit(self):
        for thing in bullets:
            if thing is PlayerBullet and self.hitbox.colliderect(thing.hitbox):
                enemies.remove(self)
                bullets.remove(thing)
  
class Bullet(pygame.sprite.Sprite):
    def __init__(self,**kwargs):
        super().__init__()
        self.hitbox = pygame.Rect(kwargs.get("start_pos",(0,0)),kwargs.get("size",(10,10)))

        self.speed = kwargs.get("speed",7)

class PlayerBullet(Bullet):
    def __init__(self,**kwargs):
        Bullet.__init__(self,**kwargs)
        self.image = pygame.image.load(os.path.join("resources","GoodBullet.png")).convert_alpha()
        pygame.draw.rect(self.image,white,self.hitbox)
        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center
        self.flag = "player's"

    def move(self):
        if self.rect.bottom >= 0 and self.hitbox.bottom >=0:
            self.rect.move_ip(0,-self.speed)
            self.hitbox.move_ip(0,-self.speed)
        else:
            bullets.remove(self)

class EnemyBullet(Bullet):
    def __init__(self,index,**kwargs):
        Bullet.__init__(self,**kwargs)
        self.index = index
        self.image = pygame.image.load(os.path.join("resources","BadBullet.png")).convert_alpha()
        pygame.draw.rect(self.image,white,self.hitbox)
        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center

    def move(self):
        if self.rect.bottom >= 0 and self.hitbox.bottom >=0:
            self.rect.move_ip(0,-self.speed)
            self.hitbox.move_ip(0,-self.speed)
        else:
            bullets.remove(self)
