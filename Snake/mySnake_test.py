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
vecSnakelist = []
testlist = []
grid = []
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
    def __init__(self, height,width,walls):
        self.width = width
        self.height = height
        self.walls = walls
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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
def shortPath(current,apple):
    if current != apple:
        pygame.draw.circle(display, (255,0,255), [int(current.x*blockSize)+blockSize/2, int(current.y*blockSize)+blockSize/2], blockSize//5)
        current2 = current + path[vec2int(current)]
        shortPath(current2,apple)
=======
def randomcheck(randApplex,randAppley,s):
    if (randApplex,randAppley) in s:
        print 'apple in snake!!!'
        newrandApplex = random.randrange(0, width - blockSize, blockSize)
        newrandAppley = random.randrange(0, height - blockSize, blockSize)
        print newrandApplex
        print newrandAppley

        return randomcheck(newrandApplex,newrandAppley,s)

    else: return [randApplex,randAppley]
>>>>>>> Stashed changes
=======
def shortPath(current,goal):
    if current != goal:
        #print ((current.x*blockSize)+(blockSize//2))
        pygame.draw.circle(display, (255,0,255), [int((current.x*blockSize)+(blockSize//2)), int((current.y*blockSize)+(blockSize//2))], blockSize//5)
        newcurrent = current + path[vec2int(current)]
        shortPath(newcurrent,goal)


def appleCreation(randApplex,randAppley,snakeList):

    if [randApplex,randAppley] not in snakeList:
        print 'GOOD APPLE'
        pygame.draw.rect(display, (255,0,0), [randApplex,randApplex, blockSize, blockSize])
>>>>>>> Stashed changes

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
            #print mpos

            if event.button == 1:
                if mpos in g.walls:
                    g.walls.remove(mpos)
                else:
                    g.walls.append(mpos)
                path = breathfirst(g,apple)

    display.fill((0,0,0))
    g = squareGrid(width//blockSize, height//blockSize,vecSnakelist[:-1])
    g.draw()

    for row in range(blockSize,width,blockSize):
        for col in range(blockSize,height,blockSize):
            #line(0, row , width, row)
            #line(col, 0, col, height)
            grid.append([row//blockSize,col//blockSize])
            cross(row, col, 3)

<<<<<<< Updated upstream


=======
     #apple
>>>>>>> Stashed changes

    posX += posX_change
    posY += posY_change

    if posX >= width-blockSize or posX <= 0 :
        posX_change = 0
    if posY >= height-blockSize or posY <= 0:
        posY_change = 0

    snakeList.append((posX,posY))
<<<<<<< Updated upstream
    s = set(snakeList[:-1])





    newapple = randomcheck(randApplex,randAppley,s)
    randApplex = newapple[0]
    randAppley = newapple[1]

    print newapple


    pygame.draw.rect(display, (255,0,0), [randApplex, randAppley, blockSize, blockSize]) #apple
=======
    vecSnakelist.append(vec(posX//blockSize,posY//blockSize))


    if len(snakeList) > snakeLength:
        del snakeList[0]
    if len(vecSnakelist) > snakeLength:
        del vecSnakelist[0]

    appleCreation(randApplex,randAppley,snakeList)

    apple = vec(randApplex//blockSize,randAppley//blockSize)
    path = breathfirst(g,apple)
    #print path
>>>>>>> Stashed changes
    """
    for node, dir in path.items():
        if dir:
            x,y = node
            pygame.draw.rect(display, (20,20,20), [x*blockSize, y*blockSize, blockSize, blockSize])
    """

<<<<<<< Updated upstream
    print 'lenght of snake is {}'.format(len(snakeList))

    if len(snakeList) > 1:
        for i in snakeList[:-1]:
            k = vec(i)//blockSize
            print k
            g.walls.append(k)


    if posX == randApplex and posY == randAppley:
        print('nom nom nom')
        randApplex = random.randrange(0, width - blockSize, blockSize)
        randAppley = random.randrange(0, height - blockSize, blockSize)
        snakeLength += 1
=======
>>>>>>> Stashed changes




    snakehead = snakeList[-1]

<<<<<<< Updated upstream
    path = breathfirst(g,apple)
    #print path

=======
>>>>>>> Stashed changes
    vecHead = vec(snakehead[0]//blockSize,snakehead[1]//blockSize)

    print 'head is '+ str(vecHead)
    print 'apple is '+ str(apple)
    print 'vecSnake is '+str(vecSnakelist[:-1])
    print 'Snake is '+str(snakeList[:-1])

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    current =  vec2int(vecHead)  + path[vec2int(vecHead)]

    shortPath(current,apple)

    """
    while current != apple:
        pygame.draw.rect(display, (255,0,255), [current.x*blockSize, current.y*blockSize, blockSize, blockSize])
        current = current + path[vec2int(current)]
    """
=======
    current = vec(vecHead)
=======
    if posX == randApplex and posY == randAppley:
        print('nom nom nom')
        #randApplex = random.randrange(0, width - blockSize, blockSize)
        #randAppley = random.randrange(0, height - blockSize, blockSize)
        snakeLength += 1
>>>>>>> Stashed changes

    while current != apple:
        pygame.draw.rect(display, (255,0,255), [current.x*blockSize+(blockSize/3), current.y*blockSize+(blockSize/3), blockSize/4, blockSize/4])
        try : current = current + path[vec2int(current)]
        except : gameOn = False 
>>>>>>> Stashed changes

<<<<<<< Updated upstream
    pygame.draw.rect(display, (0,255,0), [vecHead[0]*blockSize, vecHead[1]*blockSize, blockSize, blockSize])

<<<<<<< Updated upstream
=======
    snake(snakeList)

    for bodypart in snakeList[:-1]:
        if posX == bodypart[0] and posY == bodypart[1]:
            pygame.draw.rect(display, (0,255,255), [posX, posY, blockSize, blockSize])
            print ('self-intersect')

    g.walls = []
>>>>>>> Stashed changes
=======
    try:
        current = vecHead + path[vec2int(vecHead)]
        shortPath(current,apple)

    except: pass
    #print current

>>>>>>> Stashed changes

    #print snakehead
    clock.tick(10)
    pygame.display.update()
