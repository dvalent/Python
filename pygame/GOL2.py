import pygame
from pygame.locals import *
import random

pygame.init()

height = 600
width = 600
rows = 75
cols = 75

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
        self.pos = []
        self.collection = [ vec(1,0),    vec(-1,0),
                            vec(0,1),    vec(0,-1),
                            vec(1,1),    vec(1,-1),
                            vec(-1,-1),  vec(-1,1)]
        self.newState = []
    # create cells
    def board(self):
        self.cells = [[bool(random.randint(0,1)) for j in range(self.rows)] for i in range(self.cols)]
        self.pos = [[vec(i,j) for j in range(self.rows)] for i in range(self.cols)]
        print 'board created'
        print self.cells

    def show(self):
        return [[self.draw(i,j) for j in range(self.rows) if self.cells[i][j] == True] for i in range(self.cols)]

    def draw(self,x,y):
        return pygame.draw.ellipse(display,(255,255,255),Rect(x*bw,y*bh,bw,bh))

    def processCell(self, cell):
        count = 0
        for i in self.collection:
            if cell + i:
                count += 1
        return count

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
        self.board()
        self.show()


gameOn = True

G = grid(rows, cols)
G.board()

while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    display.fill((51,51,51))

    G.show()

    pygame.display.update()
