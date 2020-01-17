#Selection sort



#step 1: i = 0
#step 2: if i >= n-1 go to step 11 (for counting the iterations)
#step 3: minimum no of the list is   i = index_min
#step 4: j = i+1
#step 5: if j <= n go to step 9
#step 6: if list[j] < list[index_min]
#         go to step 7
#         else go to step 8

#step 7: index_min = j (set the next value) i could be written as i+1 since j = i+1
#step 8: j = j+1 ( compare with the next one and go on)
#step 9: if i != index_min then swap list[i] & list[index_min]
#step 10: i = i+1 and go to step 2
#step 11: the list is sorted



def selection_sort(a_list):
    n = len(a_list)
#finding the lowest value of the list
    for i in range(0,n-1):
        index_min = i
        

        for j in range(i+1,n):
            if a_list[j] < a_list[index_min]:
                index_min = j
#comparing the lowest value with the value of a_list[i] which is changing with each iterations
        if index_min != i:
            a_list[i],a_list[index_min] = a_list[index_min],a_list[i] #swapping


if __name__ == "__main__":
    data_list = []
    # number of elemetns as input 
    n = int(input("Enter number of elemens:")) 
  
    # iterating till the range 
    for i in range(0, n): 
        element = int(input())
        data_list.append(element)
    print("list before sorting:",data_list)
    selection_sort(data_list)
    print("list after sorting:",data_list)
    

        
        
