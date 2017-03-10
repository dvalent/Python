import pygame
from pygame.locals import *
import random
from collections import deque

vec = pygame.math.Vector2
pygame.init()

blockSize = 20
height = 320+blockSize
width = 320+blockSize
grey =(50,50,50)
print (height//blockSize)
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

class squareGrid:
    def __init__(self, height,width):
        self.width = width
        self.height = height
        self.walls = []
        self.connections = [vec(1,0), vec(-1,0), vec(0,1), vec(0,-1)]

    def inbounds(self, node):
        return 0<= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node):
        return node not in self.walls

    def neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        neighbors = filter(self.inbounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return (list(neighbors))

    def draw(self):
        for wall in self.walls:
            rect = pygame.draw.rect(display, (50, 50, 50), (wall[0]*blockSize, wall[1]*blockSize, blockSize, blockSize ))

def line(x,y,x1,y1):
    pygame.draw.line(display,grey,(x,y),(x1,y1))

def cross(x,y,crossSize):
    pygame.draw.line(display,grey,  (x-(crossSize/2),y),
                                    (x+(crossSize/2),y))
    pygame.draw.line(display,grey,  (x,y-(crossSize/2)),
                                    (x,y+(crossSize/2)))

def snake(snakeList):
    snakehead = snakeList[-1]
    snakebody = snakeList[:-1]
    for pt in snakebody:
        snakeB = pygame.draw.rect(display, (255, 255, 255), (pt[0], pt[1], blockSize, blockSize ))
    snakeH = pygame.draw.rect(display, (0, 255, 0), (snakehead[0], snakehead[1], blockSize, blockSize ))

g = squareGrid(width//blockSize, height//blockSize)

def vec2int(v):
    return (int(v.x),int(v.y))

def breathfirst(graph,start):
    frontier = deque()
    frontier.append(start)
    path = {}
    #path[vec2int(start)] = None

    while len(frontier) > 0:
        current = frontier.popleft()

        for next in graph.neighbors(current):
            if vec2int(next) not in path:
                frontier.append(next)
                path[vec2int(next)] = current - next

    return path


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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = vec(pygame.mouse.get_pos()) // blockSize
            print mpos

            if event.button == 1:
                if mpos in g.walls:
                    g.walls.remove(mpos)
                else:
                    g.walls.append(mpos)
                path = breathfirst(g,apple)

    display.fill((0,0,0))
    g.draw()
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

    """
    for node, dir in path.items():
        if dir:
            x,y = node
            pygame.draw.rect(display, (20,20,20), [x*blockSize, y*blockSize, blockSize, blockSize])
    """
    if len(snakeList) > snakeLength:
        del snakeList[0]

    if posX == randApplex and posY == randAppley:
        print('nom nom nom')
        randApplex = random.randrange(0, width - blockSize, blockSize)
        randAppley = random.randrange(0, height - blockSize, blockSize)
        snakeLength += 1

    snake(snakeList)

    for bodypart in snakeList[:-1]:
        if posX == bodypart[0] and posY == bodypart[1]:
            pygame.draw.rect(display, (0,255,255), [posX, posY, blockSize, blockSize])
            print ('self-intersect')

    apple = vec(randApplex//blockSize,randAppley//blockSize)
    snakehead = snakeList[-1]

    path = breathfirst(g,apple)
    #print path

    vecHead = (snakehead[0]//blockSize,snakehead[1]//blockSize)

    print 'head is '+ str(vecHead)
    print 'apple is '+ str(apple)

    """
    while current != apple:
        pygame.draw.rect(display, (255,0,255), [current.x*blockSize, current.y*blockSize, blockSize, blockSize])
        current = current + path[vec2int(current)]


    """

    #print snakehead
    clock.tick(10)
    pygame.display.update()
