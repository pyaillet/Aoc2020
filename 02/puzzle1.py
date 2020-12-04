#!/usr/bin/env python3

valid = 0
with open('input.txt', 'r') as f:
    row = f.readline()
    while len(row) > 0:
        spec = row.split(':')[0].split(' ')
        mini = int(spec[0].split('-')[0])
        maxi = int(spec[0].split('-')[1])
        letter = spec[1]
        password = row.split(':')[1].strip()
        if password.count(letter) >= mini and password.count(letter) <= maxi:
            valid += 1

        row = f.readline()

print(valid)
