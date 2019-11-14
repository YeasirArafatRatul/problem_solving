def main(a,b):
    count = 0
    carry = 0
    for _ in range(9,-1,-1):
        carry = a%10 + b%10 + carry
        if carry > 9:
            carry = 1
        else:
            carry = 0
        count += carry
        a //= 10
        b //= 10
    if count == 0:
      print('No carry operation.')
    elif count == 1:
      print(f'{count} carry operation.' )
    else:
      print(f'{count} carry operations.')
        



if __name__ == "__main__":
    while True:
        a,b = list(map(int,input().split()))
        if a==0 and b == 0:
            break
        else:
            main(a,b)
            
