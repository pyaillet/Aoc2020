#!/usr/bin/env python3

import sys

inp = 'test.txt'
if len(sys.argv) == 2:
    inp = sys.argv[1]

rules = {}
other_tickets = []

with open(inp, 'r') as f:
    row = f.readline().strip()
    while len(row) > 0:
        rule_name = row.split(': ')[0]
        rule_values = row.split(': ')[1]
        min1 = int(rule_values.split(' or ')[0].split('-')[0])
        max1 = int(rule_values.split(' or ')[0].split('-')[1])
        min2 = int(rule_values.split(' or ')[1].split('-')[0])
        max2 = int(rule_values.split(' or ')[1].split('-')[1])
        rules[rule_name] = (min1, max1, min2, max2)
        row = f.readline().strip()

    row = f.readline().strip()
    my_ticket = [int(v) for v in f.readline().strip().split(',')]

    row = f.readline().strip()
    row = f.readline().strip()
    row = f.readline().strip()
    while len(row) > 0:
        ticket = [int(v) for v in row.split(',')]
        other_tickets.append(ticket)
        row = f.readline().strip()

def validate_ticket(t):
    invalid_values = []
    for v in t:
        valid = False
        for rule_name in rules:
            r = rules[rule_name]
            if (v >= r[0] and v <= r[1]) or (v >= r[2] and v <= r[3]):
                valid = True
        if not valid:
            invalid_values.append(v)

    return (len(invalid_values)==0, invalid_values)

invalid_values_sum = 0
for t in other_tickets:
    v, values = validate_ticket(t)
    invalid_values_sum += sum(values)

print(invalid_values_sum)




