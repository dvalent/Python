"""GRID CLASS."""


import pygame


class grid():

    def __init__(self, screen, height, width, blockSize):
        self.height = height
        self.width = width
        self.blockSize = blockSize
        self.row = height // blockSize
        self.col = width // blockSize
        self.screen = screen
        self.posArray = []
        self.posList = []
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

    def show(self):
        for i in range(self.row):
            for j in range(self.col):
                pygame.draw.rect(self.screen, [
                                 51, 51, 51], (
                                 i * self.blockSize,
                                 j * self.blockSize,
                                 self.blockSize,
                                 self.blockSize),
                                 1)

    def position(self, test):
        for i in range(self.row):
            rowArray = []
            for j in range(self.col):
                rowArray.append([i, j])
            self.posArray.append(rowArray)
        # return self.posArray
        return (test[0] // self.blockSize, test[1] // self.blockSize)

    def list(self):
        for i in range(self.row):
            for j in range(self.col):
                self.posList.append([i, j])
        return self.posList

    def neighbors(self, test):
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        nList = []
        for i in neighbors:
            x = test[0] + i[0]
            y = test[1] + i[1]
            if x >= 0 and x <= self.width and y >= 0 and y <= self.height:
                nList.append((x, y))
        return nList
