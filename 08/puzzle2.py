#!/usr/bin/env python3

import copy
import sys

instructions = []
with open('input.txt', 'r') as f:
    row = f.readline()
    while len(row) > 0:
        inst = {'op':row.split(' ')[0],'op1':int(row.split(' ')[1])}
        instructions.append(inst)
        row = f.readline()
instructions.append({'op':'vic', 'op1':None})

class prog:
    def __init__(self, instructions):
        self.acc_val = 0
        self.ip = 0
        self.instructions = instructions
        self.ran_inst = set()

    def run_inst(self):
        if self.ip in self.ran_inst:
            print(self.acc_val)
            return False
        if self.ip > len(self.instructions):
            return False
        cur = self.instructions[self.ip]
        self.ran_inst.add(self.ip)
        return prog.__dict__[cur['op']](self, cur['op1'])
    
    def jmp(self, op1):
        self.ip += op1
        return True

    def nop(self, op1):
        self.ip += 1
        return True

    def acc(self, op1):
        self.acc_val += op1
        self.ip += 1
        return True

    def vic(self, op1):
        print('Found: {}'.format(self.acc_val))
        sys.exit(0)

    def find_loop(self):
        while self.run_inst():
            pass

for i in range(0, len(instructions)):
    new_inst = copy.deepcopy(instructions)
    if new_inst[i]['op'] in ['nop', 'jmp']:
        if new_inst[i]['op'] == 'jmp':
            new_inst[i]['op'] = 'nop'
        elif new_inst[i]['op'] == 'nop':
            new_inst[i]['op'] = 'jmp'
        print(new_inst)
        print(instructions)
        print('---')

        test = prog(new_inst)
        test.find_loop()

