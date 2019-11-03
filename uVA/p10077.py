#problem solved
#but for the language it is taking more time to execute

res = ""
mcenter = 1
ncenter = 1
    
mleft = 0
nleft = 1
    
mright = 1
nright = 0

while True:
    m, n = list(map(int, input().split()))
    if m == 1 and n == 1:
        break
    

    while mcenter != m  or ncenter != n :
        if m * ncenter > n * mcenter: # R
            mleft = mcenter
            nleft = ncenter
            res += "R"
        else: # L
            mright = mcenter
            nright = ncenter
            res += "L"
        mcenter = mleft + mright #1
        ncenter = nleft + nright #2

print(res)
