def bigSorting(unsorted):
    unsorted.sort()
    return (unsorted)

#different
def bigSorting2(unsorted):
    unsorted.sort(key = lambda x : (len(unsorted),x))
    return(unsorted)



if __name__ == "__main__":
    data_list = []
    # number of elemetns as input 
    n = int(input()) 
  
    # iterating till the range 
    for i in range(0, n): 
        element = int(input())
        data_list.append(element) # adding the element
 
    print(bigSorting2(data_list))
