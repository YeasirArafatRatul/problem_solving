
def combination(arr, n, r,index, data, i):
    
    # Current combination is ready to be printed, print it 
    if(index == r):
        for j in range(r):
                print(data[j], end = " ")  
        print()
        return

  
    # When no more elements are there to put in data[] 
    if(i >= n): 
        return

  
    # current is included,put next at next location  
    data[index] = arr[i] 
    combination(arr, n, r,index + 1, data, i + 1) 

      
    # current is excluded, replace it with  next
    #(Note that i+1 is passed, but index is not changed) 
    combination(arr, n, r, index,data, i + 1) 
  



if __name__ == '__main__':
    r = 6
    test_case = 0
    while True:
        arr = list(map(int,input().split()))
        if str(arr[0]) == "0":
            break
        else:
            if test_case > 0:
                print("")
            arr.remove(arr[0])
            n = len(arr)
            if n < 6:
                break
            else:
                # A temporary array to store all combination one by one 
                data = list(range(r))
                combination(arr, n, r,0, data, 0)
                test_case += 1
            
  
