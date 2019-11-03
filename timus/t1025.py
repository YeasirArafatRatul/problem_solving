from math import ceil
k = int(input())

supporters = list(map(int,input().split(' ')))

print(ceil(sum(supporters)/k))
