import sys

q = int(input().strip())

for a0 in range(q):
    n = int(input().strip())
    my_list = []
    for item in range(n):
       data = [int(k) for k in input().strip().split(' ')]
       my_list.append(data)
       
    sv=[]
    sh=[]
    for i in range(n):
        sv.append(0)
        sh.append(sum(my_list[i]))
        print(sv)
        print(sh)
        for j in range(n):
            sv[i]+= my_list[j][i]
    sv.sort()
    sh.sort()
    print(sv)
    print(sh)
    if sv==sh:
        print("Possible")
    else:
        print("Impossible")
