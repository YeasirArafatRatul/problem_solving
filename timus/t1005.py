n = int(input())

a_list = list(map(int,input().split(' ')))
minimum_list = []
for i in range(len(a_list)-1):
    if a_list[i] >= a_list[i+1]:
        val = a_list[i] - a_list[i+1]
    else:
        val = a_list[i+1] - a_list[i]
    minimum_list.append(val)

print(min(minimum_list))
'''  

N = int(input())
weight = list(map(int, input().split(' ')))


S = [0] + weight
K = sum(S)
X = K//2+1
Y = len(S)+1
P = []

for i in range(X):
    P.append([])
    for j in range(Y):
        if i == 0:
            P[i].append(1)
        else:
            P[i].append(0)

for i in range(1, X):
    for j in range(1, Y):
        if (i - S[j-1]) >= 0:
            P[i][j] = (P[i][j-1] or P[i - S[j-1]][j-1])
        else:
            P[i][j] = (P[i][j-1])

for i in range(X-1, -1, -1):
    if 1 in P[i]:
        print(K - 2*i)
        break
'''
