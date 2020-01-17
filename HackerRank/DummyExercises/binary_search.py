import sys

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
if __name__ == __main__ :
	 data_list = list(int(input()).sep(","))
	 data_to_find = int(input())
	 sorted_data_list = data_list.sort()
	 
	 binary_search = (sorted_data_list,data_to_find)