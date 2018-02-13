
from move_patterns import *
import pygame

FPS = 60
width = 800
height = 608
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
white = (255,255,255) #RGB
black = (0,0,0)
score = 0
bullets = []
enemies = []
move_pat = {1: figure_eight, 2: circular,3: loops}

