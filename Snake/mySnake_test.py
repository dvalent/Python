import pygame
import random

pygame.init()


blockSize = 20
height = 320+blockSize
width = 320+blockSize
grey =(50,50,50)
snakeList = []
snakeLength = 1

randApplex = random.randrange(0, width - blockSize, blockSize)
randAppley = random.randrange(0, height - blockSize, blockSize)

posX_change = 0
posY_change = 0

if (height/blockSize)%2 == 0 or (width/blockSize)%2 == 0:
    posX = (width/2)
    posY = (height/2)
else:
    posX = ((width-blockSize)/2)
    posY = ((height-blockSize)/2)

display = pygame.display.set_mode([height,width])
name = pygame.display.set_caption('DV Test')
clock = pygame.time.Clock()

def line(x,y,x1,y1):
    pygame.draw.line(display,grey,(x,y),(x1,y1))

def cross(x,y,crossSize):
    pygame.draw.line(display,grey,  (x-(crossSize/2),y),
                                    (x+(crossSize/2),y))
    pygame.draw.line(display,grey,  (x,y-(crossSize/2)),
                                    (x,y+(crossSize/2)))

def snake(snakeList):
    for pt in snakeList:
        snake = pygame.draw.rect(display, (255, 255, 255), (pt[0], pt[1], blockSize, blockSize ))



gameOn = True

while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                posX_change = 0
                posY_change = -blockSize
            if event.key == pygame.K_DOWN:
                posX_change = 0
                posY_change = blockSize
            if event.key == pygame.K_LEFT:
                posX_change = -blockSize
                posY_change = 0
            if event.key == pygame.K_RIGHT:
                posX_change = blockSize
                posY_change = 0



    display.fill((0,0,0))

    for row in range(blockSize,width,blockSize):
        for col in range(blockSize,height,blockSize):
            #line(0, row , width, row)
            #line(col, 0, col, height)
            cross(row, col, 3)

    pygame.draw.rect(display, (255,0,0), [randApplex, randAppley, blockSize, blockSize]) #apple

    posX += posX_change
    posY += posY_change

    if posX >= width-blockSize or posX <= 0 :
        posX_change = 0
    if posY >= height-blockSize or posY <= 0:
        posY_change = 0

    snakeList.append((posX,posY))

    if len(snakeList) > snakeLength:
        del snakeList[0]

    if posX == randApplex and posY == randAppley:
        print('nom nom nom')
        randApplex = random.randrange(0, width - blockSize, blockSize)
        randAppley = random.randrange(0, height - blockSize, blockSize)
        snakeLength += 1

    snake(snakeList)
    print len(snakeList)
    clock.tick(10)
    pygame.display.update()
