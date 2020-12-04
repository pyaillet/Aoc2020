#!/usr/bin/env python3

tab = []
with open('input.txt', 'r') as f:
    while True:
        try:
            tab.append(int(f.readline().strip()))
        except:
            break

for i in range(0, len(tab)):
    for j in range(i, len(tab)):
        if tab[i] + tab[j] == 2020:
            print("{} + {} = 2020 - {} * {} = {}".format(tab[i], tab[j], tab[i], tab[j], tab[i]*tab[j]))
            break
            
print(tab)
