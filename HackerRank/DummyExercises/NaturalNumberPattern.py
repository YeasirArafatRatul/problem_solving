n=int(input("Enter a number: "))
for j in range(1,n+1):
    a=[]
    for i in range(1,j+1):
        print(i,end=" ")
        if(i<j):
            print("+",end=" ")
        a.append(i)
    print("=",sum(a))
 
print()
