import sys
from math import sqrt
array = []

for line in input():
    array.append(int(line))
    
array.reverse()
for i in array:
    print("%.4f" %sqrt(i))
    
'''
while True:
    a = list(map(int,input().split()))
    a.reverse()
    for i in a:
    
        print("%.4f" %sqrt(i))
'''

'''
import sys, math
nums = []
for line in sys.stdin:
   for word in line.split():
      nums.append(float(word))
nums.reverse()
for num in nums:
   print("%.4f" % math.sqrt(num))
'''
