"""Iterative"""
def binary_search(item_list,item):
     
    item_list.sort()
    print(item_list)
    lowest = 0
    highest = len(item_list) - 1  


    while (lowest <= highest):
        mid = (lowest + highest) // 2
        
        if item_list[mid] == item:
            print(f"Item found  in position: {mid} after sorting" )
            break
        
            
        else:
            if item < item_list[mid]:
                highest = mid - 1
                
            else:
                lowest = mid + 1
                
        
    
if __name__ == "__main__":
    data_list = []
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        element = int(input())
        data_list.append(element) # adding the element
    print(data_list) #for checking 
    item = int(input("Enter item to search: "))
    call = binary_search(data_list,item)


#data_list = [1,2,4,5,7,3,8]
#tem = 5

