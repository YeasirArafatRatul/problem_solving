#insertion sort

def insertion_sort(a_list):
    n = len(a_list)

    for i in range(1,n):
        #assign the vlaue of a_list[i] in the variable item 
        item = a_list[i]

        j = i-1
        while j >= 0 and a_list[j] > item:
            a_list[j+1] = a_list[j]
            j = j-1
            a_list[j+1] = item

if __name__ == "__main__":
    L = [2,4,1,5,6]
    print("before sorting",L)
    insertion_sort(L)
    print("after_sorting",L)

    
"""
for i = 1 item = 4
then j= i-1
      =1-1
      =0
aList[0] = 2 is not greater than item = 4

(so the program will not enter in while loop)


for i = 2 item = 1 
then j= i-1
      =2-1
      =1
aList[1] = 4 is  greater than item = 1
(so the program will enter in the while loop)

alist[1+1=2] = alist[1]
             = 4
             then j = j-1
                    =1-1
                    =0
             alist[j+1/0+1=1] = item which is 1 (swapped the value)
             list after this step = [2,1,4,5,6]
             now,
             j = 0 so
             a_list[0] = 2 and item = 1
             so, a_list[j] is less than item
             so it will again enter in the while loop and swap the value
             after this iteration the list is = [1,2,4,5,6]
"""
"""
complexity of insertion sort is O(n^2)
if the list is sorted first then it is O(n) cz it will execute the for loop
"""
