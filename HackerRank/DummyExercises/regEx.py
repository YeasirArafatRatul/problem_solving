import re

string = 'Python is the easiest programming language and may be the best'

matchResult = re.match('Python is the easiest programming language and may be the best, Python',string,re.M|re.I)

if matchResult:
    print("Match Found:\n" + matchResult.group())
else:
    print("Match Not Found")


searchResult = re.search("Python",string,re.M|re.I)
if searchResult:
    print("Search Found:" + searchResult.group())
else:
    print("Search Not Found")
