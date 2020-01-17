# formkeys

d = {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}
print(d)
d = dict.fromkeys(['name', 'age', 'height'], 'unknown')  # output will be same
print(d)
e = dict.fromkeys("abc", 'unknwon')  # abc will be splited
print(e)
# 1 to 10 every numbers value will be 'unknwon'
e = dict.fromkeys(range(1, 11), 'unknwon')
print(e)

print(d.get('names'))

d1 = d.copy()
d = d.clear
