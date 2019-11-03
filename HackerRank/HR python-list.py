L=[]
N = int(input())

for row in range(N):
    inputs = input().split()
    if len(inputs)==1:
        command =inputs[0]
    if len(inputs)==2:
        command = inputs[0]
        e = int(inputs[1])
    if len(inputs)==3:
        command = inputs[0]
        i = int(inputs[1])
        e = int(inputs[2])

    if command=="insert":
        L.insert(i,e)
    elif command=="remove":
        L.remove(e)
    elif command=="append":
         L.append(e)
    elif command=="sort":
         L.sort()
    elif command=="pop":
         L.pop()
    elif command=="reverse":
         L.reverse()
    elif command=="print":
         print(L)
