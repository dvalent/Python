import pygame
from pygame.locals import *

pygame.init()

height = 500
width = 500

display = pygame.display.set_mode([height,width])
name = pygame.display.set_caption('DV Test')
clock = pygame.time.Clock()


gameOn = True

while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    display.fill((0,0,0))

    clock.tick(10)

    pygame.display.update()
