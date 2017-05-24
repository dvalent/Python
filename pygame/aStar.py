import math
import pygame
import Queue as Q


class aStar():
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end

    def heuristic(self, node):
        d = math.sqrt(abs((node[0] - self.end[0])) +
                      abs((node[1] - self.end[1])))
        return d

    def Start(self):
        frontier = Q.PriorityQueue()
        frontier.put(self.start, 0)
        came_from = {}
        cost = {}
        came_from[self.start] = None
        cost[self.start] = 0

        while not frontier.empty() > 0:
            current = frontier.get()
            if current == self.end:
                break
            print self.grid.neighbors(current)
            for next in self.grid.neighbors(current):
                new_cost = cost[current] + self.grid.cost(current, next)
                print new_cost
                print next
                print current
                if next not in cost or new_cost < cost[next]:
                    cost[next] = new_cost
                    priority = new_cost + self.heuristic(next)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost
