def type_selection(a_list):
    string = []
    number = []
    for i in a_list:
        if i.isnumeric():
            a = int(i)
            number.append(a)
        else:
            string.append(i)
    return string,number

count = int(input("Number of items:"))
a_list = []
for i in range(count):
    j = input()
    a_list.append(j)
result = type_selection(a_list)
print(result)
