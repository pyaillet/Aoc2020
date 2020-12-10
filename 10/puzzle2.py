#!/usr/bin/env python3

inp = 'input.txt'

from itertools import chain, combinations

def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

f = open(inp, 'r')
rows = [int(r.strip()) for r in f.readlines()]
rows.sort()
rows.insert(0, 0)

def split_groups(rows):
    groups = []
    prec = 0
    cur = []
    for i in rows:
        if i - prec == 3:
            groups.append(cur)
            cur = []
            cur.append(i)
        else:
            cur.append(i)
        prec = i
    groups.append(cur)
    return groups

def valid_group(group, test):
    prec = group[0]
    test.append(group[-1])
    print(group, test)
    for i in test:
        if i - prec > 3:
            print("KO")
            return False
        prec = i
    print("Ok")
    return True

def count_for_group(group):
    if len(group) <= 2:
        print("{} => {}".format(group, 1))
        return 1
    count = 0
    for test in powerset(group[1:-1]):
        if valid_group(group, list(test)):
            count += 1
    print("* {} => {}".format(group, count))
    return count

def count_possibilities(groups):
    product = 1
    for g in groups:
        product = product * count_for_group(g)
    return product

print(split_groups(rows))
print(count_possibilities(split_groups(rows)))

