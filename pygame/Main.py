"""GAME MAIN."""

import pygame
from gridClass import grid
from aStar import aStar


pygame.init()
screen = pygame.display.set_mode((400, 400))
name = pygame.display.set_caption('DV Test')
clock = pygame.time.Clock()
blockSize = 20


GameOn = True
while GameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOn = False
    mousePos = pygame.mouse.get_pos()

    mainGrid = grid(screen, 400, 400, blockSize)
    mainGrid.show()
    screen.fill([0, 0, 0])
    gridpos = mainGrid.position(mousePos)
    mouseGrid = (gridpos[0], gridpos[1])
    # print mouseGrid
    pygame.draw.rect(screen, [255, 0, 0], (gridpos[0] * blockSize,
                                           gridpos[1] * blockSize,
                                           blockSize,
                                           blockSize))

    mainGrid.show()
    neigh = mainGrid.neighbors(gridpos)

    for n in neigh:
        pygame.draw.rect(screen, [238, 198, 6], (n[0] * blockSize,
                                                 n[1] * blockSize,
                                                 blockSize,
                                                 blockSize))
    #start = mouseGrid
    start = (0, 0)
    end = [5, 7]

    a = aStar(mainGrid, start, end)

    pygame.draw.rect(screen, [255, 0, 233], (end[0] * blockSize,
                                             end[1] * blockSize,
                                             blockSize,
                                             blockSize))
    # print mouseGrid

    print aStar.heuristic(a, start)
    print aStar.Start(a)

    pygame.display.flip()
