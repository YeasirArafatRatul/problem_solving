def linear_search(a_list, x):
    n = len(a_list)
    i = 0

    while i < n:
        if a_list[i] == x:
            print(x, "is found in ", i ,"position in list")

        i += 1


a = [2, 3, 4, 5, 2, 6,5]
x = 5

call = linear_search(a,x)