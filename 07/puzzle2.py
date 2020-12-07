#!/usr/bin/env python3

rules = {}
with open('input.txt', 'r') as f:
    row = f.readline().strip()
    while len(row) > 0:
        head = row.split(' contain ')[0][:-5]
        if row.split(' contain ')[1] == 'no other bags.':
            leaves = []
        else:
            leaves = [{'count': int(s[:-4].strip()[:2]),'type': s[:-4].strip()[2:]} for s in row.split(' contain ')[1][:-1].split(',')]
        rules[head] = leaves
        row = f.readline().strip()

def count(bag):
    total = 0
    for l in rules[bag]:
        total += l['count']
        total += count(l['type'])*l['count']
    return total

print(rules)
print(count('shiny gold'))

