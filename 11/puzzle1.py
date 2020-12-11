#!/usr/bin/env python3

import sys

inp = 'test.txt'
if len(sys.argv) >= 2:
    inp = sys.argv[1]

f = open(inp, 'r')
rows = [r.strip() for r in f.readlines()]

def is_free(i, j, rows):
    if i < 0 or i >= len(rows):
        return False
    if j < 0 or j >= len(rows[i]):
        return False
    if rows[i][j] == 'L':
        return True
    return False

def is_occupied(i, j, rows):
    if i < 0 or i >= len(rows):
        return False
    if j < 0 or j >= len(rows[i]):
        return False
    if rows[i][j] == '#':
        return True
    return False
    
def find_occupied(x, y, rows):
    count = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if is_occupied(i, j, rows):
                if i != x or j != y:
                    count += 1
    return count


def simulate_round(rows):
    new_rows = []
    changes = 0
    for i in range(0, len(rows)):
        row = ''
        for j in range(0, len(rows[i])):
            if is_free(i, j, rows):
                if find_occupied(i, j, rows) == 0:
                    changes += 1
                    row += '#'
                else:
                    row += 'L'
            elif is_occupied(i, j, rows):
                if find_occupied(i, j, rows) >= 4:
                    changes += 1
                    row += 'L'
                else:
                    row += '#'
            else:
                row += '.'
            

        new_rows.append(row)
    return (changes, new_rows)

def count_occupied(rows):
    count = 0
    for r in rows:
        count += r.count('#')
    return count

rounds = 0
changes = 1
while changes > 0:
    changes, rows = simulate_round(rows)
    rounds += 1

print((changes, rows))
print(rounds)
print(count_occupied(rows))

