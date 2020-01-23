#has errors

k = int(input())
input()

out = []

def get(a_list,index):
    return(a_list[index])


for i in range(k):
    m,n = input().split()

    elementsAdded = list(map(int,input().split()))
    getsAfter = list(map(int,input().split()))

    
    p = 0
    for j in range(len(elementsAdded)):
        out.append(elementsAdded[j])
        out.sort()
        maxi = max(out)
        
        if p <= getsAfter[p] and getsAfter[p] <= maxi:
            print(get(out,p))
            p += 1



