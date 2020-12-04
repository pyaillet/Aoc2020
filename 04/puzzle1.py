#!/usr/bin/env python3

import re

passports = []
with open('input.txt', 'r') as f:
    tmp = {}
    row = f.readline()
    while len(row) > 0:
        print(row)
        if len(row.strip().split(' ')[0].split(':')) < 2:
            passports.append(tmp)
            tmp = {}
            next
        for field in row.strip().split(' '):
            if len(field) > 0:
                tmp[field.split(':')[0]] = field.split(':')[1]
        row = f.readline()
passports.append(tmp)

print(len(passports))

count = 0
mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for p in passports:
    msg = ''
    valid = True
    for m in mandatory:
        if not m in p:
            valid = False
            msg += 'Missing field: {}'.format(m)
            break

    if valid:
        count += 1
        print('Valid passport: {}'.format(p))
    else:
        pass
        print('Invalid passport: {} - {}'.format(p, msg))
    #t = input()

print(count)

    

