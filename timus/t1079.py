def maximum(n):
    
    for i in range(2,n+1):
        try:
            if (i%2):
                array[i] = array[i//2] + array[i//2+1]
            else:
                array[i] = array[i//2]

            maxi[i] = max(array[i],maxi[i-1])
        except IndexError:
            print(f"List index out of range for i = {i}")

    return maxi[n]


    
if __name__ == "__main__":
    array = [0]*100000
    maxi = [0]*100000
    array[1] = 1
    maxi[1]=1
  
    for _ in range(10):
        n = int(input())
        if n != 0:
            print(maximum(n))
        else:
            break

