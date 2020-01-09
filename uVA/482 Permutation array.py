n = int(input())


for j in range(n):
    input()
    line1 = list(map(int,input().split()))
    line2 = list(map(str,input().split()))
    
    dictionary = {}
    for i in range(len(line1)):
        dictionary[line1[i]] = line2[i]

    for i in sorted(line1):
        print(dictionary[i])
        
    if j < n-1:
        print()

    
