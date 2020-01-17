"""different methods for taking a list input"""
def function_one():
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(input_numbers)


def function_two():
    data_list = []
   
    n = int(input())
  
    for i in range(0, n): 
        element = int(input())
        data_list.append(element) 
    print(data_list)

def function_three():
    a = list(map(int, input().split()))
    print(a)

    
