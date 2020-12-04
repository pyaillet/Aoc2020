#!/usr/bin/env python3

rows = []
with open('input.txt') as f:
    row = f.readline()
    while len(row) > 0:
        rows.append(row.strip())
        row = f.readline()

i = 1
j = 3
count = 0
while i < len(rows):
    if rows[i][j] == '#':
        count += 1
    i += 1
    j = (j + 3) % len(rows[0])
print(count)


