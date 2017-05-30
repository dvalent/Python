import pygame
from pygame.locals import *

height = 800
width = 800
white = (255,255,255)
grey = (21,21,21)
black = (0,0,0,0.5)
red = (255,0,0)

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((width,height))
pygame.display.set_caption('DV')

block_x = width/2
block_y = height/2
block_size = 20
FPS = 30

running = True
while running:
    block_x_move = 0
    block_y_move = 0

    for event in pygame.event.get():
        #print 'event: '+str(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block_x_move = -block_size
                block_y_move = 0
            if event.key == pygame.K_RIGHT:
                block_x_move = block_size
                block_y_move = 0
            if event.key == pygame.K_UP:
                block_x_move = 0
                block_y_move = -block_size
            if event.key == pygame.K_DOWN:
                block_x_move = 0
                block_y_move = block_size

    s = pygame.Surface((width,height), pygame.SRCALPHA)
    s.fill((0,0,0,25))
    display.blit(s, (0,0))
    for row in range(block_size,width+block_size,block_size):
        for col in range(block_size,height+block_size,block_size):
            pygame.draw.line(display,grey,(row,0),(row,height),1)
            pygame.draw.line(display,grey,(0,col),(width,col),1)

            
    block_x += block_x_move
    block_y += block_y_move


    block = pygame.draw.rect(display,white,[block_x,block_y,block_size,block_size])






    clock.tick(FPS)
    pygame.display.flip()
