from functools import reduce

#greatest common divisor(gorishtho sadharon gunoniyouk)
def compute_gcd(x,y):
    #find the smaller 
    smaller = min(x,y)
    gcd = 1
    for i in range(1,smaller+1):
        if((x%i == 0) and (y%i==0)):
            #gcd will be alterted each time the condition is  true, so do
            #not need find the maximum.
            gcd = i
    #print(gcd)
    return gcd

#least common multiplier(logistho sadharon gunitok)

def compute_lcm(a,b):
    factor = a*b
    gcd = compute_gcd(a,b)
    lcm = factor // gcd
    #print(lcm)
    return lcm


def getTotalX(arrayA, arrayB):
 
    min_gcd = reduce(compute_gcd, arrayB)
    #print(min_gcd)
    max_lcm = reduce(compute_lcm, arrayA)
    #print(max_lcm)
    count = 0
    
    #          start_value,stop_value,difference in each iteration
    for x in range(max_lcm, min_gcd+1, max_lcm):
        if min_gcd % x == 0:
            count += 1
 
    return count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
