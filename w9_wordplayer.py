# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:01:23 2016

@author: NelsonWang
"""
from itertools import combinations, permutations
from sys import argv, exit

script, dataset = argv
library = dict()
f = open(argv[1], 'r')
# read file into dict library
while True:
    line = f.readline()
    line = line.strip('\n')
    temp = sorted(line)
    for letter in temp:
        key = ''.join(temp)
    library.setdefault(key, [])
    # key in library is alphabetical order of line
    library[key].append(line)
    if not line:
        break

for item in library:
    print(item, library[item])


# read input
line = input()
x = line.split(' ')
wordInput, wordLength = x[0], int(x[1])
# sort wordInput into alphabetical order in order to get from library
tempInputSorted = sorted(wordInput)

for letter in tempInputSorted:
    word = ''.join(tempInputSorted)
# raise Error if wordLength is bigger than word length
if len(word) < wordLength:
    raise ValueError
# all the combinations C(wordLength/word length)
keylist = permutations(word, wordLength)
klist = []

for item1 in keylist:
    klist.append(''.join(item1))
"""
print (klist)
print (".")
"""
for item2 in klist:
    while True:
        if klist.count(item2) == 1:
            break
        klist.remove(item2)
"""
for item2 in klist:
    print(item2)
"""
for item2 in klist:
    if library.get(item2, default=None) is not None:
        print(library.values(item2))

print(".")

exit(0)
