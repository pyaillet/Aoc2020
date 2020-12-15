#!/usr/bin/env python3

import sys

inp = 'input.txt'
num = 30000000
if len(sys.argv) == 3:
    inp = sys.argv[1]
    num = int(sys.argv[2])

nums = {}
init = []
for n in open(inp, 'r').readline().split(','):
    init.append(int(n))

prec = 0
for i in range(0,num):
    if i < len(init):
        cur = init[i]
    elif prec in nums:
        cur = i - nums[prec]
    else:
        cur = 0
    #print(cur, prec, i)
    if i != 0:
        nums[prec] = i
    prec = cur
    #print(nums)
print(cur)
