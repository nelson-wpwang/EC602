# -*- coding: utf-8 -*-

from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib

def natsort(list_):
    # decorate
    tmp = [ (int(re.search('\d+', i).group(0)), i) for i in list_ ]
    tmp.sort()
    # undecorate
    return [ i[1] for i in tmp ]
listDir = listdir()
matching_pic = [i for i in listDir if "png" in i]
img_no_white_dict = {}
img_match_dict = {}
result_file = open("ans1.txt","w")
hash_file = open("hash.txt","w")
newline = "\n"
for i in matching_pic:
    img_temp = imread(i, as_grey=True)
    
    img_no_white_index = np.nonzero(img_temp != 1)

    row_low_index = np.amin(img_no_white_index[0])
    row_high_index = np.amax(img_no_white_index[0])+1
    column_low_index = np.amin(img_no_white_index[1])
    column_high_index = np.amax(img_no_white_index[1])+1

    img_no_white = img_temp[row_low_index:row_high_index, column_low_index:column_high_index]

    img_row_sum = np.around(np.sum(img_no_white, axis=1),decimals=4)
    img_column_sum = np.around(np.sum(img_no_white, axis=0),decimals=4)

    list_temp = []
    list_temp.append(i)
    list_temp.append(img_row_sum)
    list_temp.append(img_column_sum)
    list_temp.append(img_no_white.shape)

    sum_img_no_white = "%.9f" % np.sum(img_no_white)
    if sum_img_no_white in img_no_white_dict:
        img_no_white_dict[sum_img_no_white].append(list_temp)
    else:
        img_no_white_dict[sum_img_no_white] = [list_temp]

for j in img_no_white_dict.keys():
    list_temp_search = img_no_white_dict[j]
    if len(list_temp_search) == 1:
        # only one item, which can put into identity list/dict directly
        img_match_dict[list_temp_search[0][0]] = [list_temp_search[0][0]]
        
    else:
        for sub_list_temp_search in list_temp_search:
            if sub_list_temp_search[3][0] > sub_list_temp_search[3][1]:
                sub_list_temp_search[3] = (sub_list_temp_search[3][1],sub_list_temp_search[3][0])
                sub_list_temp_search[1],sub_list_temp_search[2] = sub_list_temp_search[2],sub_list_temp_search[1]
            # print(sub_list_temp_search)
        # print(list_temp_search[0][1][::-1])
        flag = True
        while flag:
            equal_list_temp = [list_temp_search[0][0]]
            temp = [0]
            for m in range(1,len(list_temp_search)):
                if list_temp_search[0][3] == list_temp_search[m][3]:
                    if (list_temp_search[0][1]-list_temp_search[m][1]).all() == (list_temp_search[0][2]-list_temp_search[m][2]).all():
                        equal_list_temp.append(list_temp_search[m][0])
                        temp.insert(0,m)
                    elif (list_temp_search[0][1]-list_temp_search[m][1][::-1]).all() == (list_temp_search[0][2]-list_temp_search[m][2]).all():
                        equal_list_temp.append(list_temp_search[m][0])
                        temp.insert(0,m)
                    elif (list_temp_search[0][1]-list_temp_search[m][1]).all() == (list_temp_search[0][2]-list_temp_search[m][2][::-1]).all():
                        equal_list_temp.append(list_temp_search[m][0])
                        temp.insert(0,m)
                    elif (list_temp_search[0][1]-list_temp_search[m][1][::-1]).all() == (list_temp_search[0][2]-list_temp_search[m][2][::-1]).all():
                        equal_list_temp.append(list_temp_search[m][0])
                        temp.insert(0,m)
            for i in temp:
                del list_temp_search[i]
            equal_list_temp = natsort(equal_list_temp)
            img_match_dict[equal_list_temp[0]] = equal_list_temp
            if len(list_temp_search) == 0:
                flag = False
for i in natsort(img_match_dict.keys()):
    equal_list_temp_str = ' '.join(img_match_dict[i]) + newline
    result_file.writelines(equal_list_temp_str)
result_file.close()
f = open("ans1.txt","rb")
m = hashlib.sha256(f.read()).hexdigest()
hash_file.write("The output of " + "\n" + "python w11_duplicatefinder.py"  + "\n" +"in this directory should be " + "\n" + m)
hash_file.close()

