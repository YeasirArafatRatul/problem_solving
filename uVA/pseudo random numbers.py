'''
hare and tortoise loop detection algorithm
or
brent's cycle detection algorithm
'''

def loop_detection(func,seed):
    power = count = 1
    tortoise = seed #first_node
    hare = func(seed) #calling the function to give the next value

    while tortoise != hare:
        if power == count:
            tortoise = hare #now tortoise has forward to hare's position
            power *= 2
            count = 0
        
        hare = func(hare) #hare is forwarding to the next random number 
        count +=1
        #print(f'count : {count}, power: {power}')
    return count


case = 1    
while True:
    Z,I,M,L = map(int, input().split())
    if Z == I== M == L == 0:
        break
    else:
        def next_value_counter(L):
            return (Z*L+I)%M
        print(f"Case {case}: {loop_detection(next_value_counter,L)}")
        case += 1
