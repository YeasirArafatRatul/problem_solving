#first method
for i in range(int(input())):
    if i==0:
        pass
    else:
        print(i,end="")
print(i+1)

#2nd method
print(*range(1, int(input()) + 1), sep="")


#3rd method
n = int(input())
for i in range(n+1):
    if i==0:
        continue
    print(i,end="")
