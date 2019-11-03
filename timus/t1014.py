#solved
#author arafat ratul
n = int(input())
if n == 0:
    print(10)
elif n == 1:
    print(1)
else:
    valid = True
    minimum_str = ''

    while valid and n != 1:
        valid = False
        
        for i in range(9,1,-1):
            if n%i == 0:
                valid = True
                minimum_str += str(i)
                n /= i
                break

    if valid != True:
        print("-1 \n")
    else:
        print(minimum_str[::-1])
'''
first_digit = int(minimum_str)
second_digit = n//first_digit
if first_digit*second_digit == n:
    print(str(first_digit)+str(second_digit))
'''
