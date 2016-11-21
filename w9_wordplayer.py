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

# 咱们之前用搜索的思路是，从输入的temp2和b combinations后出来的list对应搜索dictionary里的key值
# 如果combinations出来的结果不多还好，如果多了的话效率就会降低，这是我们就换一个方法搜索
# 我们反向从dictionary中的key值去看输入的文字a中是否有自己的字母，如果都有的话就当作结果输出
# 这个是大体思路，详细的解释在下面
while True:
    result = list()
    line = input()
    x = line.split()
    a, b = x[0], int(x[1])
    if b == 0:
        break
    temp2 = sorted(a)
        
    #这里加的判定规则小于1/4大于3/4是我自己设定的值
    #当b的值在word长度一半左右的时候，combinations的数量最多，此时用第二种方法搜索
    if b < len(temp2) / 4 or b > 3 * len(temp2) / 4:
        for letter in temp2:
            word = ''.join(temp2)
            keylist = combinations(word, b)
            #把keylist强行设置成set能够把里面重复的值去掉
            klist = list(set(keylist))

        for index in klist:
            if (''.join(index)) in library:
                #extend可以把一个list里的元素全添加到另一个list里
                #可以替代之前的判断和循环
                result.extend(library[''.join(index)])
    else:
        for key in library:
            temp3 = sorted(a)
            #如果key的长度和要求的长度相等才进行接下来的操作
            if len(key) == b:
                #我们一个字母一个字母地看key中的字幕是否在我们输入搜索的a中
                for i in key:
                    #如果a中有key的字母，则从中移除
                    if temp3.count(i) != 0:
                        temp3.remove(i)
                #比对移除key中所有字母的temp3的长度是否和输入的a的长度和b的差相同
                #若相同，则说明这个key中的字母在输入的a中都有，则确认是我们要搜索的项
                #若不同，则说明输入的a中不包含这个key中的所有字母，说明不是我们要搜索的项
                if len(temp3) == len(temp2) - b:
                    result.extend(library[''.join(key)])

    if result:
        print(('\n'.join(sorted(result))))
    print('.')
