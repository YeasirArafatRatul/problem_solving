
n, k = map(int, input().split())
S = map(int, input().split())


def Subset(S, k, n):
    r = [0] * k
     
    for value in S:
        r[value%k] += 1
     
    count = 0
    
    for a in range(1, (k+1)//2):
        count += max(r[a], r[k-a])
    if k % 2 == 0 and r[k//2]:
        count += 1
    if r[0]:
        count += 1
    return count
     

print(Subset(S, k, n))

