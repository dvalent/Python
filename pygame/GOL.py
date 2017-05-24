import pygame
from pygame.locals import *

pygame.init()

height = 500
width = 500
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
        self.collection = [ vec(1,0),    vec(-1,0),
                            vec(0,1),    vec(0,-1),
                            vec(1,1),    vec(1,-1),
                            vec(-1,-1),  vec(-1,1)]

    def vectors(self):
        return [[cell(i, j) for j in range(self.rows)] for i in range(self.cols)]
    def show(self):
        return [[j.draw() for j in i]  for i in self.vectors()]
    def inbounds(self,node):
        return 0 <= node.x < self.cols and 0 <= node.y < self.rows
    def neighbors(self,node):
        n = [node + j for j in i for i in self.collection]
        return filter(self.inbounds , n)

class cell():
    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
        self.state = False
    def setstate(self,newstate):
        self.state = newstate
    def pos(self):
        return vec(self.posX , self.posY)
    def draw(self):
        return pygame.draw.ellipse(display,(255,255,255),Rect(self.posX*bw,self.posY*bh,bw,bh))

gameOn = True

G = grid(rows, cols)
#print G.vectors()

while gameOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    display.fill((51,51,51))

    G.show()



    clock.tick(10)

    pygame.display.update()
