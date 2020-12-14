#!/usr/bin/env python3

import sys

inp = 'test.txt'
if len(sys.argv) == 2:
    inp = sys.argv[1]

f = open(inp, 'r')

time = int(f.readline())
buses = list(map(int, filter(lambda x: x != 'x', f.readline().strip().split(','))))

def next_bus(x):
    t = time
    return (x, (int(t/x)+1)*x % t)

def earliest(x):
    return x[1]

print((time, buses))

bus = min(list(map(next_bus, buses)), key=earliest)
print(bus)

print(bus[0]*bus[1])
