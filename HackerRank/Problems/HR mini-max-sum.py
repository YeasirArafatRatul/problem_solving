def mini_max(a_list):
    mini_max_list = []
    total = sum(a_list)
    for i in a_list:
        result =total- i
        mini_max_list.append(result)


    print(min(mini_max_list),end=" ")
    print(max(mini_max_list))
a = [1,2,3,4,5]
output = mini_max(a)

