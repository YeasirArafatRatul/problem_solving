
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr,n):
    size_of_list = n
    list_of_elements = arr

    positive = 0
    negative = 0
    neutral = 0

    for element in list_of_elements:
        if element > 0:
            positive += 1
        elif element < 0:
            negative += 1
        elif element == 0:
            neutral += 1


    print("%.6f" % float(float(positive/size_of_list)))
    print("%.6f" % float(float(negative/size_of_list)))
    print("%.6f" % float(float(neutral/size_of_list)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
