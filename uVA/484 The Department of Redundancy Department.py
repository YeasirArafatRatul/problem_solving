redundancy_free = []
copy_of_the_list = []
while True:
    try:
        the_list = list(map(int,input().split()))
        for i in the_list:
            copy_of_the_list.append(i)
            if i not in redundancy_free:
                redundancy_free.append(i)
            else:
                continue
    except EOFError:
        break

for i in redundancy_free:
    a = copy_of_the_list.count(i)
    print(f'{i} {a}')
