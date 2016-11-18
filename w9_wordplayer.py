# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:01:23 2016

@author: NelsonWang
"""
from itertools import combinations
from sys import argv, exit

script, dataset = argv
library = dict()
f = open(argv[1], 'r')
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
wordInput, wordLength = x[0], int(x[1])
tempInputSorted = sorted(wordInput)

for letter in tempInputSorted:
    word = ''.join(tempInputSorted)
keylist = combinations(word, wordLength)
klist = []

for item in keylist:
    klist.append(''.join(item))
'print (klist)'
for item in klist:
    while True:
        if klist.count(item) == 1:
            break
        klist.remove(item)

for item in klist:
    print(item)

for item in klist:
    if library.get(item, default=None) is not None:
        print(library.values(item))

print(".")

exit(0)
