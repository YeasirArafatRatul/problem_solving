#Bubble Sort Algorithm

#step 1: take input a list and the numbers of the list
#step 2: i = 0
#step 3: if i < n go to step 4
#        else go to step 8
#step 4: j = 0
#step 5: if j < (n-i-1) go to step 6
#        else go to step 7
#step 6: if a_list[j] > a_list[j+1] then SWAP them
#step 7: j = j+1 and go to step 5
#step 8: i = i+1 and go to step 3
#step 9: End, the list is sorted


#implementation

def bubble_sort(a_list,n):
    for i in range (0,n):
        for j in range(0,n-i-1):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]

if __name__ == "__main__":
    n = int(input("Enter the number of element:"))

    a_list=[]

    for i in range(0,n):
        element = int(input())
        a_list.append(element)
        
    print("before sorting:",a_list)

    bubble_sort(a_list,n)
        
    print(a_list)


#Time Complexity = O(n^2)
    
# O(n*(n-i-1)) #how many times the loops will iterate
#O(n*(n-1) --> second loop will iterate the most when i = 0
#O(n^2 -n)
#O(n^2) # because n is very small in compareable to n^2
