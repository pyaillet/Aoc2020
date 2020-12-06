#!/usr/bin/env python3

groups = []
with open('input.txt', 'r') as f:
    row = f.readline()
    group = ""
    while len(row) > 0:
        if row != "\n":
            group += row.strip()
        else:
            groups.append(set(group))
            group = ""

        row = f.readline()
    groups.append(set(group))


print(sum(map(lambda x: len(x), groups)))
        
