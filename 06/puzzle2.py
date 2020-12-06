#!/usr/bin/env python3

groups = []
with open('input.txt', 'r') as f:
    row = f.readline()
    group = None
    while len(row) > 0:
        if row != "\n":
            if group == None:
                group = set(row.strip())
            else:
                group = group.intersection(set(row.strip()))
        else:
            groups.append(group)
            group = None

        row = f.readline()
    groups.append(group)

print(groups)


print(sum(map(lambda x: len(x), groups)))
        
