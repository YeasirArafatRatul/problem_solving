'''
hare and tortoise loop detection algorithm
or
brent's cycle detection algorithm
'''

def loop_detection(func,seed):
    power = lam = 1
    tortoise = seed #first_node
    hare = func(seed) #calling the function to give the next value

    while tortoise != hare:
        if power == lam:
            tortoise = hare
            power *= 2
            lam = 0
        hare = func(hare)
        lam +=1


    tortoise = hare = seed
    for i in range(lam):
        hare = func(hare)
    while tortoise != hare:
        tortoise = func(tortoise)
        hare = func(hare)
      
    return lam



case = 1    
while True:
    Z,I,M,L = map(int, input().split())
    if Z== I== M == L == 0:
        break
    else:
        def next_value_counter(L):
            return (Z*L+I)%M
        print(f"Case {case}: {loop_detection(next_value_counter,L)}")
        case += 1
        
