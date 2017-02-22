import pygame
import time
import random

pygame.init()

###VARIABLES###

white = (255, 255, 255)
black = (0, 0, 0)
dRed = (85, 0, 0)
red = (128, 22, 22)
pink = (212, 106, 106)
lPink = (255, 170, 170)
green = (0,155,0)

displayWidth = 800
displayHeight = 600

clock = pygame.time.Clock()

blockSize = 10

FPS = 50

font = pygame.font.SysFont(None, 25)


def snake(blockSize,snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], blockSize, blockSize])


def text_objects(text, color):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()


def message(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (displayWidth / 2, displayHeight / 2)
    gameDisplay.blit(textSurf,textRect)

    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [displayWidth / 2, displayHeight / 2])


###GAMESETUP###

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Slither')


###GAME LOOP###

def gameLoop():

    gameExit = False
    gameOver = False

    lead_x = displayWidth / 2
    lead_y = displayHeight / 2

    lead_x_change = 0  # ???
    lead_y_change = 0  # ???

    snakeList = []
    snakeLength = 1

    randApplex = random.randrange(0, displayWidth - blockSize, 10)
    randAppley = random.randrange(0, displayHeight - blockSize, 10)

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message('Game Over press C to play again or Q to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -blockSize
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = blockSize
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    lead_y_change = -blockSize
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = blockSize
                    lead_x_change = 0

        if lead_x >= displayWidth or lead_x < 0 or lead_y >= displayHeight or lead_y < 0:
            gameOver = True

            ''' ###STOP THE SNAKE###
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                       '''

        lead_x += lead_x_change  # AHH this is the updated position! lead x > original position
        lead_y += lead_y_change

        gameDisplay.fill(dRed)
        pygame.draw.rect(gameDisplay, white, [randApplex, randAppley, blockSize, blockSize]) #apple

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True


        snake(blockSize, snakeList)


        pygame.display.update()

        if lead_x == randApplex and lead_y == randAppley:
            print('nom nom nom')
            randApplex = random.randrange(0, displayWidth - blockSize, 10)
            randAppley = random.randrange(0, displayHeight - blockSize, 10)
            snakeLength += 1

        clock.tick(FPS)

    print(event)

    message('YOU LOOSE!', lPink)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()


gameLoop()
