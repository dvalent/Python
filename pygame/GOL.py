import pygame
from pygame.locals import *
import random

pygame.init()

height = 600
width = 600
rows = 120
cols = 120

bh = height//rows
bw = width//cols

display = pygame.display.set_mode([width,height])
clock = pygame.time.Clock()
name = pygame.display.set_caption('Game of Life {}'.format(clock.get_fps()))

vec = pygame.math.Vector2

class grid():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.collection = [ vec(1,0),    vec(-1,0),
                            vec(0,1),    vec(0,-1),
                            vec(1,1),    vec(1,-1),
                            vec(-1,-1),  vec(-1,1)]
        self.newState = []
    # create cells
    def vectors(self):
        self.cells = [[cell(i, j) for j in range(self.rows)] for i in range(self.cols)]
    #set intial state
    def randomState(self):
        return [[j.setState(True) for j in i if random.randint(1,5) ==  1]  for i in self.cells]
    #draw cells
    def show(self):
        return [[j.draw() for j in i if j.getState() == True] for i in self.cells]

    # too many for loop debug with one and get rid of inbounds def TRY/EXCEPT
    def inbounds(self,node):
        return 0 <= node.x < self.cols and 0 <= node.y < self.rows

    def neighbors(self,node):
        n = [node + i for i in self.collection]
        return filter(self.inbounds , n)

    def eval(self):
        for i in self.cells:
            for j in i:
                count = 0
                try:
                    n = [self.cells[int((j.pos() + i).x)][int((j.pos() + i).y)].getState() for i in self.collection] #vector position not cell class
                    trueOnes = sum(n)
                    #print trueOnes
                except:
                    pass
                    #print 'Error out bounds'
                """
                vecNeighbors = [(int(k.x),int(k.y)) for k in self.neighbors(j.pos())]
                vecState = [self.cells[x][y].getState() for x,y in vecNeighbors]
                trueOnes = sum(vecState)
                #print "cell {} has {} neighbors {} {} {}".format(j.pos(),len(vecNeighbors),vecNeighbors,vecState,trueOnes)
                """
                if j.getState() == True:
                    if trueOnes < 2:
                        j.setNext(False)
                    elif trueOnes <= 3:
                        j.setNext(True)
                    elif trueOnes >= 4:
                        j.setNext(False)
                else:
                    if trueOnes == 3:
                        j.setNext(True)

    def swapState(self):
        return [[j.swap() for j in i]  for i in self.cells]


    def run(self):
        self.vectors()
        self.randomState()

class cell():
    def __init__(self,posX,posY):
        self.posX   = posX
        self.posY   = posY
        self.state  = False
        self.NextState = False
    def setState(self,newstate):
        self.state = newstate
        return self.state
    def getState(self):
        return self.state
    def pos(self):
        return vec(self.posX , self.posY)
    def draw(self):
        return pygame.draw.ellipse(display,(255,255,255),Rect(self.posX*bw,self.posY*bh,bw,bh))
    def setNext(self,next):
        self.NextState = next
    def swap(self):
        self.state = self.NextState

gameOn = True

G = grid(rows, cols)
G.run()


while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    display.fill((51,51,51))

    G.show()
    G.eval()
    G.swapState()

    #clock.tick(100)

    pygame.display.update()
