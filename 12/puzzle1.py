#!/usr/bin/env python3

import sys

inp = 'test.txt'
if len(sys.argv) >= 2:
    inp = sys.argv[1]

instructions = [(r[0], int(r[1:])) for r in open(inp,'r').readlines()]

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
card = {'E':0,'S':1,'W':2,'N':3}
turn = {'R': 1, 'L': -1}

class boat:
    def __init__(self, instructions):
        self.instructions = instructions
        self.pos = [0, 0]
        self.dir = 0
        self.cur = 0

    def step(self):
        cur = self.instructions[self.cur]
        if cur[0] in card:
            self.move(cur[1], card[cur[0]])
        if cur[0] == 'F':
            self.move(cur[1], self.dir)
        if cur[0] in turn:
            self.turn(cur[1], turn[cur[0]])

    def move(self, dist, direction):
        for i in range(0, 2):
            self.pos[i] += dist * directions[direction][i]

    def turn(self, amount, mult):
        self.dir = int((self.dir + amount * mult / 90) % 4)

    def run(self):
        for i in range(0, len(instructions)):
            self.cur = i
            self.step()

b = boat(instructions)
b.run()

print(sum([abs(i) for i in b.pos]))
