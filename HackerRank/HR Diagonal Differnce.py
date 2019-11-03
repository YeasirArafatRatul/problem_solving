"""
*****WRONG*****
def difference(arr, n): 
  
    # Initialize sums of diagonals 
    d1 = 0
    d2 = 0
  
    for i in range(1, n+1): 
      
        for j in range(1, n+1): 
          
            # finding sum of primary diagonal 
            if (i == j): 
                d1 += arr[i][j] 
  
            # finding sum of secondary diagonal 
            if (i+j == n+1): 
                d2 += arr[i][j] 
          
    # Absolute difference of the sums 
    # across the diagonals 
    return abs(d1 - d2);

ERROR: IndexError: list index out of range
"""
  
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(array,n):
  
    # Initialize sums of diagonals 
    d1 = 0
    d2 = 0
  
    for i in range(0, n): 
      
        for j in range(0, n): 
          
            # finding sum of primary diagonal 
            if (i == j): 
                d1 += arr[i][j] 
  
            # finding sum of secondary diagonal 
            if (i == n - j - 1): 
                d2 += arr[i][j] 
          
    # Absolute difference of the sums 
    # across the diagonals 
    return abs(d1 - d2);
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []


    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
