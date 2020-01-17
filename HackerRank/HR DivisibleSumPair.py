'''
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n,k,a_list):
    count = 0

    for i in range(n+1):
        for j in range(i+1,n):
            if (a_list[i] + a_list[j])% k == 0:
                count += 1
    return count




if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().strip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)


'''
#for HUNT PYTHON book

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(a_list,k):
    count = 0

    for i in range(len(a_list)+1):
        for j in range(i+1,len(a_list)):
            if (a_list[i] + a_list[j])% k == 0:
                count += 1
    return count

if __name__ == '__main__':
    ar = list(map(int, input().strip().split()))
    k = int(input())
    result = divisibleSumPairs(ar, k)

    print(result)
