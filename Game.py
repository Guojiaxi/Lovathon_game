from math import *
import pygame, os

class Player(object):
    def __init__(self):
        self.box = pygame.Rect(width/2, height/2, 50, 50)

    def move(self, dx, dy):
        if dx != 0 or dy != 0:
            self.move_xy(dx, dy)

    def move_xy(self, dx, dy):
        self.box.move_ip(dx,0)
        self.box.move_ip(0,dy)

        for wall in walls: # COLLISION DETECTION
            if self.box.colliderect(wall.box):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.box.right = wall.box.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.box.left = wall.box.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.box.bottom = wall.box.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.box.top = wall.box.bottom



os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
running = True

width = 800
height = 608
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("game")

white = (255,255,255) #RGB
black = (0,0,0)

clock = pygame.time.Clock()
player = Player()

speed = 5

for x in range(0,width,16):
    walls.append(Wall([x,0],16,16))

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # basic movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-speed,0)
    if key[pygame.K_RIGHT]:
        player.move(speed,0)
    if key[pygame.K_UP]:
        player.move(0,-speed)
    if key[pygame.K_DOWN]:
        player.move(0,speed)

    #draw
    screen.fill(white)
    for wall in walls:
        pygame.draw.rect(screen, (128,128,128), wall.box, 0)
    pygame.draw.rect(screen, black, player.box, 0)
    pygame.display.flip()



pygame.quit()
