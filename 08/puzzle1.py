#!/usr/bin/env python3

instructions = []
with open('input.txt', 'r') as f:
    row = f.readline()
    while len(row) > 0:
        inst = {'op':row.split(' ')[0],'op1':int(row.split(' ')[1])}
        instructions.append(inst)
        row = f.readline()

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
        self.ran_inst.add(self.ip)
        cur = self.instructions[self.ip]
        prog.__dict__[cur['op']](self, cur['op1'])
        return True
    
    def jmp(self, op1):
        self.ip += op1

    def nop(self, op1):
        self.ip += 1

    def acc(self, op1):
        self.acc_val += op1
        self.ip += 1


    def find_loop(self):
        while self.run_inst():
            print(self.__dict__)
            pass

test = prog(instructions)
test.find_loop()
