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

def value_valid_for_field(value, field):
    v = value
    r = rules[field]
    return (v >= r[0] and v <= r[1]) or (v >= r[2] and v <= r[3])
    

def validate_ticket(t):
    invalid_values = []
    for v in t:
        valid = False
        for rule_name in rules:
            if value_valid_for_field(v, rule_name):
                valid = True
        if not valid:
            invalid_values.append(v)

    return invalid_values

valid_tickets = list(filter(lambda t: len(validate_ticket(t)) == 0, other_tickets))
valid_tickets.append(my_ticket)

fields_values = []
for i in range(0, len(my_ticket)):
    fields_values.append([t[i] for t in valid_tickets])

valid_fields_for_value = []
for idx, values in enumerate(fields_values):
    valid_fields = []
    for rule_name in rules:
        if len(list(filter(lambda v: not value_valid_for_field(v, rule_name), values))) == 0:
            valid_fields.append(rule_name)
    valid_fields_for_value.append((idx, valid_fields))

valid_fields_for_value.sort(key=lambda s: len(s[1]))

def remove_field(valid_fields,f):
    for cur_field in valid_fields:
        try:
            cur_field[1].remove(f)
        except:
            pass
    return valid_fields

rules_idx = {}

while len(valid_fields_for_value) > 0:
    if len(valid_fields_for_value[0][1]) > 1:
        print('Error')
        sys.exit()
    cur_rule = valid_fields_for_value[0][1][0]
    rules_idx[cur_rule] = valid_fields_for_value[0][0]
    valid_fields_for_value = valid_fields_for_value[1:]
    remove_field(valid_fields_for_value, cur_rule)

p = 1
for k in rules_idx:
    if k.startswith('departure'):
        p = p * my_ticket[rules_idx[k]]
print(p)





