def perfection_checker(integer):
    total = 1
    if integer > 1:
        for i in range(2,integer//2+1):
            if integer%i==0:
                total += i

        if total > integer:
            print(f"{integer:>5}  ABUNDANT")
        elif total < integer:
            print(f"{integer:>5}  DEFICIENT")
        else:
            print(f"{integer:>5}  PERFECT")
    else:
        print(f"{integer:>5}  DEFICIENT")
     

if __name__ == "__main__":
    print("PERFECTION OUTPUT")
    end = False
    while True:
        l = list(map(int,input().split()))
        for i in l:
            if i == 0:
                end = True
                break
            else:
                perfection_checker(i)

        if end:
            print("END OF OUTPUT")
            break

'''
***test_case***
for j in range(2,100):
    print(f"=======for {j}========")
    perfection_checker(j)
'''
