# AUTHOR Wenpeng Wang wpwang@bu.edu
# AUTHOR Yuxuan Su suyuxuan@bu.edu
# AUTHOR Yihan Li liyihan@bu.edu

from itertools import combinations
from sys import argv, exit

script, dataset = argv
library = dict()
f = open(argv[1], 'r')

l = f.read()
for line in l.split():
    temp = sorted(line)
    for letter in temp:
        key = ''.join(temp)
    library.setdefault(key, [])
    library[key].append(line)

while True:
    result = list()
    line = input()
    x = line.split()
    a, b = x[0], int(x[1])
    if b == 0:
        break
    temp2 = sorted(a)

    if b < len(temp2) / 4 or b > 3 * len(temp2) / 4:
        for letter in temp2:
            word = ''.join(temp2)
            keylist = combinations(word, b)
            klist = list(set(keylist))

        for index in klist:
            if (''.join(index)) in library:
                result.extend(library[''.join(index)])
    else:
        for key in library:
            temp3 = sorted(a)
            if len(key) == b:
                for i in key:
                    if temp3.count(i) != 0:
                        temp3.remove(i)
                    if len(temp3) == len(temp2) - b:
                        result.extend(library[''.join(key)])

    if result:
        print(('\n'.join(sorted(result))))
    print('.')
