#!/usr/bin/env python3

occupied = []
with open('input.txt', 'r') as f:
    row = f.readline().strip()
    while len(row) > 0:
        s = int(row.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2)
        occupied.append(s)
        row = f.readline().strip()

occupied.sort()

print(occupied[-1])

