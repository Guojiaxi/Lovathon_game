import pygame,os,random
from globalvars import *
from move_patterns import *

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Body(pygame.sprite.Sprite):
    def __init__(self,**kwargs):
        super().__init__()

        self.hitbox = pygame.Rect(kwargs.get("start_pos",(0,0)),kwargs.get("size",(61,54)))

class Player(Body):
    def __init__(self, **kwargs):
        Body.__init__(self,**kwargs)
        self.image = pygame.image.load(os.path.join("resources","GOLD.png")).convert_alpha()
        #pygame.draw.rect(self.image,white,self.hitbox)

        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center
        self.rect.center = (width / 2, height / 2)
        self.dead = False
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
            if thing is EnemyBullet and self.rect.colliderect(thing.rect):

                all_sprites.remove(thing)
                bullets.remove(thing)
                self.image = pygame.image.load(os.path.join("resources", "GOLDDEAD.png")).convert_alpha()
                # player needs to die or lose a life
                # explosion animation
        for enemy in enemies:
            if self.hitbox.colliderect(enemy.hitbox):
                # me ded
                pass

    def collision(self):
        for thing in enemies:
            if self.rect.colliderect(thing.rect):
                self.image = pygame.image.load(os.path.join("resources","GOLDDEAD.png")).convert_alpha()
                self.dead = True


class Enemy(Body):
    def __init__(self, **kwargs):
        Body.__init__(self,**kwargs)
        self.image = pygame.image.load(os.path.join("resources", "BAD.png")).convert_alpha()
        #pygame.draw.rect(self.image, white, self.hitbox)
        self.rect = self.image.get_rect()
        self.rect.center = kwargs.get("start_pos",(0,0))
        enemies.append(self)
        self.pattern = random.randint(1,len(move_pat))
        self.t = 0
        self.nature = random.randint(0,2)

    def move(self):
        (dx,dy) = move_pat[self.pattern](self.t)
        self.rect.move_ip(dx, 0)
        self.rect.move_ip(0, dy)
        self.t += (-1)**self.nature

    def is_hit(self):
        for thing in bullets:
            if thing.players and self.rect.colliderect(thing.rect):
                all_sprites.remove(self)
                enemies.remove(self)
                all_sprites.remove(thing)
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
        #pygame.draw.rect(self.image,white,self.hitbox)
        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center
        self.players = True

    def move(self):
        if self.rect.bottom >= 0 and self.hitbox.bottom >=0:
            self.rect.move_ip(0,-self.speed)
            self.hitbox.move_ip(0,-self.speed)
        else:
            all_sprites.remove(self)
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
            all_sprites.remove(self)
            bullets.remove(self)
