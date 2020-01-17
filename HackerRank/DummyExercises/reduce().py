import functools

a = range(1,101)

print(functools.reduce(lambda x,y:x+y,a))
