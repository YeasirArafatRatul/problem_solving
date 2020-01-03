n = int(input())

for i in range(n):
    l = ""
    while l == "":
        l = input().strip()
        
    xLL1,yLL1,xUR1,yUR1 = list(map(int,l.split()))
     
    l = ""
    while l == "":
        l = input().strip()

    xLL2,yLL2,xUR2,yUR2 = list(map(int,l.split()))
        
    if xLL1 >= xUR2 or xLL2 >= xUR1 or yLL1 >= yUR2 or yLL2 >= yUR1:
        print("No Overlap")
    else:
        print(f"{max(xLL1, xLL2)} {max(yLL1, yLL2)} {min(xUR1, xUR2)} {min(yUR1, yUR2)}")
    if i < n-1:
        print()
