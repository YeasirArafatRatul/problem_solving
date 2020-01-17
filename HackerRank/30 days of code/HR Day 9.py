#n = int(input())
#for i in range (1,n):
#    dec = n-1
#    fact = n*dec
#print(fact)


n = int(input().strip())

def factorial(n):
    if n is 1:
        return 1
    else:
        return (n) * factorial(n-1)

ans = factorial(n)
print(ans)
