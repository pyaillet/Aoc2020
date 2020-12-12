#!/usr/bin/env python3

import sys
import math

inp = 'test.txt'
if len(sys.argv) >= 2:
    inp = sys.argv[1]

instructions = [(r[0], int(r[1:])) for r in open(inp,'r').readlines()]

directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
card = {'E':0,'S':1,'W':2,'N':3}
turn = {'R': -1, 'L': 1}

class boat:
    def __init__(self, instructions):
        self.instructions = instructions
        self.pos = [0, 0]
        self.waypoint = [10, 1]
        self.cur = 0

    def step(self):
        cur = self.instructions[self.cur]
        if cur[0] == 'F':
            self.move(cur[1])
        if cur[0] in turn:
            self.rotate(cur[1], turn[cur[0]])
        if cur[0] in card:
            self.move_waypoint(cur[1], card[cur[0]])

    def move(self, dist):
        for i in range(0, 2):
            self.pos[i] += self.waypoint[i] * dist

    def rotate(self, amount, mul):
        angle = math.radians(amount) * mul
        c = int(math.cos(angle))
        s = int(math.sin(angle))
        wp = [0, 0]
        wp[0] = c * self.waypoint[0] - s * self.waypoint[1]
        wp[1] = s * self.waypoint[0] + c * self.waypoint[1]
        self.waypoint = wp

    def move_waypoint(self, amount, direction):
        for i in range(0, 2):
            self.waypoint[i] += amount * directions[direction][i]

    def run(self):
        for i in range(0, len(instructions)):
            print(self.__dict__)
            self.cur = i
            self.step()

b = boat(instructions)
b.run()

print(sum([abs(i) for i in b.pos]))
