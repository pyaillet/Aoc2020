#!/usr/bin/env python3

from operator import xor

valid = 0
with open('input.txt', 'r') as f:
    row = f.readline()
    while len(row) > 0:
        spec = row.split(':')[0].split(' ')
        first = int(spec[0].split('-')[0])
        second = int(spec[0].split('-')[1])
        letter = spec[1]
        password = row.split(':')[1].strip()
        if xor(password[first-1] == letter,password[second-1] == letter):
            valid += 1

        row = f.readline()

print(valid)
