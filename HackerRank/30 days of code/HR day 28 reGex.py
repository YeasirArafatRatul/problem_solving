import math
import os
import random
import re
import sys


pattern = r'[a-z]+'
pattern_mail = r'[a-z]+\@gmail.com'

def search(a_list):
    
    names = []
    for i in a_list:
        if re.search(pattern,i) and re.search(pattern_mail,i):
            names.append(re.search(pattern,i).group())
    return sorted(names)

if __name__ == '__main__':
    N = int(input())
    a_list = []
    for N_itr in range(N):
        firstNameEmailID = input()
        a_list.append(firstNameEmailID)
        #firstName = firstNameEmailID[0]

        #emailID = firstNameEmailID[1]

    result = search(a_list)
    for i in result:
        print(i)
       
