while True:
    Z,I,M,L = map(int, input().split())
    #print(Z,I,M,L)
    if Z==0 and I==0 and M==0and L == 0:
        break
    else:
        count = 1
        old_L = L
        try:
            while True:
                L = (Z*L+I)%M
                if L == old_L:
                    break
                else:
                    #print(L)
                    count+=1

            print(f'Case: {count}')
        except EOFError:
            break
