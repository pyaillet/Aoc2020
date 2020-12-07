#!/usr/bin/env python3

rules = []
with open('input.txt', 'r') as f:
    row = f.readline().strip()
    while len(row) > 0:
        head = row.split(' contain ')[0][:-5]
        leaves = [s[:-4].strip()[2:] for s in row.split(' contain ')[1][:-1].split(',')]
        rules.append({'head': head, 'leaves': leaves})
        row = f.readline().strip()

def find(bag):
    found = []
    for r in rules:
        if bag in r['leaves']:
            found.append(r['head'])
            found.extend(find(r['head']))
    return found

print(rules)
print(set(find('shiny gold')))
print(len(set(find('shiny gold'))))

