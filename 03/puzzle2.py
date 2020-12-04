#!/usr/bin/env python3

rows = []
with open('input.txt') as f:
    row = f.readline()
    while len(row) > 0:
        rows.append(row.strip())
        row = f.readline()

increments = [
        [ 1, 1 ],
        [ 3, 1 ],
        [ 5, 1 ],
        [ 7, 1 ],
        [ 1, 2 ],
        ]

p = 1
for inc in increments:
    i = inc[1]
    j = inc[0]
    count = 0
    while i < len(rows):
        if rows[i][j] == '#':
            count += 1
        i += inc[1]
        j = (j + inc[0]) % len(rows[0])
    p = p * count
print(p)

