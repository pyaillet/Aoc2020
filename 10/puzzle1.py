#!/usr/bin/env python3

inp = 'input.txt'

f = open(inp, 'r')
rows = [int(r.strip()) for r in f.readlines()]
rows.sort()

diffs = {
        1: 0,
        2: 0,
        3: 0
        }

cur = 0
for i in range(1, max(rows)+3):
    cur += 1
    if i in rows:
        diffs[cur] += 1
        cur = 0
cur += 1
diffs[cur] += 1

print(diffs[1]*diffs[3])
