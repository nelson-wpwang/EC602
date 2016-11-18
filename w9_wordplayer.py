# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:01:23 2016

@author: NelsonWang
"""
from sys import argv, exit
from itertools import combinations


script, dataset= argv
library = dict()
f = open(argv[1],'r')
while True:
    line = f.readline()
    temp = sorted(line)
    for letter in temp:
        key = ''.join(temp)
    library.setdefault(key, [])
    library[key].append(line)
    if not line:
        break
    
'''for item in library:
    print(item, library[item])

'''
line = input()
x = line.split(' ')
a, b = x[0], int(x[1])
temp2 = sorted(a)

for letter in temp2:
    word = ''.join(temp2)
keylist = combinations(word, b)
klist = []

for item in keylist:
    klist.append(''.join(item))

for item in klist:
    while True:
        if klist.count(item) == 1:
            break
        klist.remove(item)
        

for item in klist:
    print(item)

for item in klist:
    if library.get(item, default = None) != None:
        print (library.values(item))
    
print (".")

exit(0)
