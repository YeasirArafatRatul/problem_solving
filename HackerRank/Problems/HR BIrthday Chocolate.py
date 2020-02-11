# Complete the birthday function below.
def birthday(chocolate_bars, d, m):
    count = 0
    i = 0
    while i <= len(chocolate_bars)-m:
        result = 0
        for j in range(i,m+i):
            result += chocolate_bars[j]
        if result == d:
            count += 1
        i += 1
    return count
    

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().strip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)

