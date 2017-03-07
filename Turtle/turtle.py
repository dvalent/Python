import sys, os, math, random, functools
import numpy as np
import matplotlib
import matplotlib.pyplot as pp
import matplotlib.animation as anim


class Turtle(object):
    def __init__(self):
        self.pos = (0,0)
        self.angle = 0
        self.pen = True

    def forward(self,distance):
        posnew = (  self.pos[0] + distance + math.cos(self.deg * self.angle),
                    self.pos[1] + distance + math.cos(self.deg * self.angle))

        if self.pen:
            pass

        self.pos = posnew

    def right(self, angle):
        self.angle = (self.angle - angle) % 360

    def left(self, angle):
        self.angle = (self.angle + angle) % 360

    def penup(self) :
        self.pen = False

    def pendown(self):
        self.pen = True

class terrarium(object):
    def __init__(self):
        pass

fig = pp.figure(figsize=(3,3))
axes = pp.axes()

line = pp.Line2D((0,1),(0.5,0.25))
axes.add_line(line)

axes.set_xticks([])
