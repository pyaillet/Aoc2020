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
        if m == 'byr':
            try:
                valid = int(p[m]) >= 1920 and int(p[m]) <= 2002
                if not valid:
                    msg += 'byr invalid: {}'.format(p[m])
                    break
            except:

                valid = False
                break
        if m == 'iyr':
            try:
                valid = int(p[m]) >= 2010 and int(p[m]) <= 2020
                if not valid:
                    msg += 'iyr invalid: {}'.format(p[m])
                    break
            except:
                valid = False
                msg += 'iyr invalid: {}'.format(p[m])
                break
        if m == 'eyr':
            try:
                valid = int(p[m]) >= 2020 and int(p[m]) <= 2030
                if not valid:
                    msg += 'eyr invalid: {}'.format(p[m])
                    break
            except:
                valid = False
                msg += 'eyr invalid: {}'.format(p[m])
                break
        if m == 'hgt':
            hgt = p[m][:-2]
            unit = p[m][-2:]
            if unit == 'cm':
                h = int(hgt)
                valid = h >= 150 and h <= 193
            elif unit == 'in':
                h = int(hgt)
                valid = h >= 59 and h <= 76
            else:
                valid = False
            if not valid:
                msg += 'hgt invalid: {}'.format(p[m])
                break

        if m == 'hcl':
            valid = re.match('^#[0-9a-f]{6}$', p[m])
            if not valid:
                msg += 'hcl invalid: {}'.format(p[m])
                break

        if m == 'ecl':
            valid = p[m] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if not valid:
                msg += 'ecl invalid: {}'.format(p[m])
                break
        
        if m == 'pid':
            valid = re.match('^[0-9]{9}$', p[m])
            if not valid:
                msg += 'pid invalid: {}'.format(p[m])
                break

    if valid:
        count += 1
        print('Valid passport: {}'.format(p))
    else:
        pass
        print('Invalid passport: {} - {}'.format(p, msg))
    #t = input()

print(count)

    

