import pygame,os,random,math
from globalvars import *
from math import *
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
        self.shoot_speed = 6
        self.rect = self.image.get_rect()
        # self.rect.center = self.hitbox.center
        self.rect.center = (width / 2, height / 2)
        self.dead = False
        self.shoot_timer = FPS/self.shoot_speed
        self.score = 0


    def move(self,key):
        if key[pygame.K_LSHIFT]:
            self.speed = 2
        else:
            self.speed = 4

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
        if self.shoot_timer:
            self.shoot_timer -= 1
        else:
            bullets.append(PlayerBullet(start_pos=(current_position[0]-3,current_position[1]-30), speed=15))
            self.shoot_timer = FPS/self.shoot_speed

    def is_hit(self):
        for thing in enemies:
            if self.rect.colliderect(thing.rect):
                self.image = pygame.image.load(os.path.join("resources","GOLDDEAD.png")).convert_alpha()
                self.dead = True

        for thing in bullets:
            if self.rect.colliderect(thing.rect):
                all_sprites.remove(thing)
                bullets.remove(thing)
                self.image = pygame.image.load(os.path.join("resources", "GOLDDEAD.png")).convert_alpha()
                self.dead = True
                # explosion animation

class Enemy(Body):
    def __init__(self, **kwargs):
        Body.__init__(self,**kwargs)
        self.image = pygame.image.load(os.path.join("resources", "BAD.png")).convert_alpha()
        #pygame.draw.rect(self.image, white, self.hitbox)
        self.rect = self.image.get_rect()
        self.rect.center = kwargs.get("start_pos",(0,0))
        self.shoot_timer = 120/1
        enemies.append(self)
        self.pattern = random.randint(1,len(move_pat))
        self.t = 0
        self.nature = random.randint(0,2)

    def move(self):
        (dx,dy) = move_pat[self.pattern](self.t)
        self.rect.move_ip(dx, 0)
        self.rect.move_ip(0, dy)
        self.t += (-1)**self.nature

    def is_hit(self,player):
        for thing in bullets:
            if thing.players and self.rect.colliderect(thing.rect):
                all_sprites.remove(self)
                enemies.remove(self)
                all_sprites.remove(thing)
                bullets.remove(thing)
                player.score += 1
                
    def shoot(self,currentpos,target):
        bullets.append(EnemyBullet(start_pos=currentpos,speed = 50,target=target))
        
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
    def __init__(self,**kwargs):
        Bullet.__init__(self,**kwargs)
        self.speed = 3
        self.target = kwargs.get("target",(0,0))
        self.image = pygame.image.load(os.path.join("resources","BadBullet.png")).convert_alpha()
        pygame.draw.rect(self.image,white,self.hitbox)
        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center
        self.players = False

        self.x_slope = self.rect.center[0] - self.target[0]
        self.y_slope = self.rect.center[1] - self.target[1]
        self.norm = math.sqrt(self.x_slope**2 + self.y_slope**2)
        #self.slope = self.y_slope/self.x_slope
        #self.angle = atan(self.slope)

    def move(self):
        if self.rect.bottom >= 0 and self.rect.top <= height and self.rect.left >=0 and self.rect.right <= width:
            #self.rect.move_ip(0,-self.speed)
            #self.hitbox.move_ip(0,-self.speed)
            self.rect.move_ip(-(self.x_slope*self.speed)/self.norm,-(self.y_slope*self.speed)/self.norm)
        else:
            all_sprites.remove(self)
            bullets.remove(self)
