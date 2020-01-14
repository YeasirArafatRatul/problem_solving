list_one = []
list_two = []

while True:
    height, worker = list(map(int,input().split()))
    if height == worker == 0:
        break

    if height == worker:
        v1 = 0
        v2 = height
    else:
        N = -1
        for i in range(1,32):
            n = pow(worker,1/i)
            N = int(n)
            if N**i == worker:
                if (N+1)**i == height:
                    break
            elif(N+1)**i == worker:
                if(N+2)**i == height:
                    N = N+1
                    break
            elif(N-1)**i == worker:
                if(N)**i == height:
                    N=N-1
                    break
    for j in range(i):
        item = (N**j)
        list_one.append(item)
        v1 = sum(list_one)
        
    for j in range(i+1):
        item =  ((height // ((N+1)**j))*(N)**j)
        list_two.append(item)
        v2 = sum(list_two)
    print(v1, v2)

#TME
