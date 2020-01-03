
'''
n = int(input())

for i in range(n):
    input()
    string = input()
    sliced_string = ''
    for letter in string:
        current_letter = letter
        sliced_string += letter
        if sliced_string == string[len(sliced_string):len(sliced_string)+len(sliced_string)]:
            print(len(sliced_string))
            break
    
        if i < n-1:
            print()

''' 
import re


n = int(input())
  
for i in range(n):

  input()
  string = input()
  

  power = len([m.start() for m in re.finditer(f'(?={string})', string + string)]) - 1
  
  print(len(string) // power)
  if i < n -1 :
    print()

