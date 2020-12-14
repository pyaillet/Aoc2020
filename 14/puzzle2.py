#!/usr/bin/env python3

import sys 
import itertools as it

inp = 'test.txt'

if len(sys.argv) == 2:
    inp = sys.argv[1]

class computer:
    def __init__(self, instructions):
        self.mem = {}
        self.mask = ''
        self.cur = 0
        self.instructions = instructions

    def set_mask(self, val):
        self.mask = val

    def set_mem(self, val, addr):
        addr36 = "{0:036b}".format(addr)
        new_addr = ''
        for i in range(0,36):
            if self.mask[i] == '0':
                new_addr += addr36[i]
            else:
                new_addr += self.mask[i]

        print(new_addr)
        for i in it.product('01', repeat=new_addr.count('X')):
            count = 0
            gen_addr = ''
            for b in new_addr:
                if b == 'X':
                    gen_addr += i[count]
                    count += 1
                else:
                    gen_addr += b
            self.mem[int(gen_addr, 2)] = val

    def run_step(self, ip):
        cur_inst = self.instructions[ip]
        if cur_inst[0] == 'mask':
            self.set_mask(cur_inst[1])
        elif cur_inst[0] == 'mem':
            self.set_mem(cur_inst[1], cur_inst[2])

    def run(self):
        for i in range(0, len(self.instructions)):
            self.run_step(i)

    def sum_mem(self):
        return sum([self.mem[k] for k in self.mem])


def parse_inst(s):
    arr = s.strip().split(' = ')
    if arr[0] == 'mask':
        return ('mask', arr[1])
    elif arr[0][0:3] == 'mem':
        return ('mem', int(arr[1]), int(arr[0].split('[')[1].strip(']')))

instructions = list(map(parse_inst, open(inp, 'r').readlines()))
print(instructions)
c = computer(instructions)
c.run()
print(c.sum_mem())
