# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:01:23 2016

@author: NelsonWang
"""
# AUTHOR Wenpeng Wang wpwang@bu.edu
# AUTHOR Yuxuan Su suyuxuan@bu.edu

from sys import argv, exit
from itertools import combinations


script, dataset= argv
library = dict()
f = open(argv[1],'r')
while True:
    line = f.readline()
    line = line.rstrip('\n')
    temp = sorted(line)
    for letter in temp:
        key = ''.join(temp)
    library.setdefault(key, [])
    library[key].append(line)
    if not line:
        break
    
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
  
result = list()      
for item in klist:
    if item in library:
        if type(library.get(item))==str:
            result.append(library.get(item))
        else:
            i = 0;
            while i < len(library.get(item)):
                result.append(library.get(item)[i])
                i = i + 1
result.sort()
for item in result:
    print (item)
print (".")

exit(0)
