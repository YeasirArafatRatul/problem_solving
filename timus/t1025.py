k = int(input())

supporters = list(map(int,input().split(' ')))
supporters.sort()
total = 0
for x in range(k//2+1):
    total += supporters[x]//2+1

print(total)
