import re

pattern = r'[a-zA-Z]+'
while True:
  try:
    text = str(input())
    words_list = re.findall(pattern,text)
    
    print(len(words_list))
    
  except(EOFError):
    break
