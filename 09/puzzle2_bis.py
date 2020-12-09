#!/usr/bin/env python3

from itertools import combinations

inp = 'test.txt'
preamble = 5
window = 5
inp = 'input.txt'
preamble = 25
window = 25

numbers = []
with open(inp, 'r') as f:
    row = f.readline().strip()
    while len(row) > 0:
        numbers.append(int(row))
        row = f.readline().strip()

def find_pair(c, w):
    return len(list(filter(lambda p: sum(p) == c, combinations(w, 2)))) > 0

def find_invalid_number(numbers):
    for i in range(0, len(numbers)-preamble):
        cur_w = numbers[i:(i+window)]
        cur = numbers[preamble+i]
        if not find_pair(cur, cur_w):
            return (i+preamble, cur)

(idx, target) = find_invalid_number(numbers)

def find_range(target, numbers):
    for width in range(2, len(numbers)):
        i = 0
        while i+width < len(numbers):
            window = numbers[i:i+width]
            if sum(window) == target:
                return min(window)+max(window)
            i += 1

print(find_range(target, numbers[0:idx]))
