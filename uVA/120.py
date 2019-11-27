
def flip(unsorted_list):
    working_list = unsorted_list.copy()
    #print("WORKING_LIST:", working_list)
    sorted_set = sorted(unsorted_list)
    #print(sorted_set)
    
    N = len(sorted_set)
    steps_to_sort = []
    for i in range(len(working_list)-1, -1, -1):
      # Check if ith element is sorted, sort it if not.
      index  = working_list.index(sorted_set[i])
      #print(f"for i = {i} index = {index} and sorted_i = {sorted_set[i]}")
      if index == i:
        continue

      if index == 0:
        # One Flip
        working_list[0:i+1] = working_list[0:i+1][::-1]
        #print("in index == 0 working_list:",working_list)
        steps_to_sort.append(N - i)
      else:
        # Two flips
        working_list[0:index+1] = working_list[0:index+1][::-1] #flipping
        #print("in else(1st line)working_list:",working_list)
        working_list[0:i+1] = working_list[0:i+1][::-1]
        #print("in else(2nd line) working_list:",working_list)

        steps_to_sort.append(N - index)
        steps_to_sort.append(N - i)

    steps_to_sort.append(0)
    #output
    print(" ".join(map(str, unsorted_list)))
    print(" ".join(map(str, steps_to_sort)))

    
if __name__ == "__main__":
    
    while True:
        initial_list = list(map(int,input().split()))
        try:
            flip(initial_list)
        except(EOFError):
            break
