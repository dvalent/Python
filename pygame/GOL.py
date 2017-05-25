import pygame
from pygame.locals import *
import random

pygame.init()

height = 600
width = 600
rows = 100
cols = 100

bh = height//rows
bw = width//cols

display = pygame.display.set_mode([width,height])
name = pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()

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
    # create cells
    def vectors(self):
        self.cells = [[cell(i, j) for j in range(self.rows)] for i in range(self.cols)]
    #set intial state
    def randomState(self):
        return [[j.setState(bool(random.randint(0,6))) for j in i]  for i in self.cells]
    #draw cells
    def show(self):
        return [[j.draw() for j in i if j.getState() == True] for i in self.cells]

    def inbounds(self,node):
        return 0 <= node.x < self.cols and 0 <= node.y < self.rows

    def neighbors(self,node):
        n = [node + i for i in self.collection]
        return filter(self.inbounds , n)

    def eval(self):
        for i in self.cells:
            for j in i:
                vecNeighbors = [k for k in self.neighbors(j.pos()) if self.cells[int(k.x)][int(k.y)].getState() == True]
                if j.getState() == True:
                    if len(vecNeighbors) < 2:
                        j.setState(False)
                    elif len(vecNeighbors) <= 3:
                        j.setState(True)
                    elif len(vecNeighbors) >= 4:
                        j.setState(False)
                else:
                    if len(vecNeighbors) == 3:
                        j.setState(True)


    def run(self):
        self.vectors()
        self.randomState()

class cell():
    def __init__(self,posX,posY):
        self.posX   = posX
        self.posY   = posY
        self.state  = False
    def setState(self,newstate):
        self.state = newstate
        return self.state
    def getState(self):
        return self.state
    def pos(self):
        return vec(self.posX , self.posY)
    def draw(self):
        return pygame.draw.ellipse(display,(255,255,255),Rect(self.posX*bw,self.posY*bh,bw,bh))


gameOn = True

G = grid(rows, cols)
G.run()
print



while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    display.fill((51,51,51))

    G.eval()
    G.show()





    clock.tick(100)

    pygame.display.update()
