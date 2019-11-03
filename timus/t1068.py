n = int(input())
total = 0
if n <= 0:
    for i in range(n,2):
        total += i
else:
    for i in range(1,n+1):
        total += i
print(total,"\n")
