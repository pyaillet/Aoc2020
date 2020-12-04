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
        for k in range(j, len(tab)):
            if tab[i] + tab[j] + tab[k] == 2020:
                print("{} * {} * {} = {}".format(tab[i], tab[j], tab[k], tab[k]*tab[i]*tab[j]))
                break
            
print(tab)
