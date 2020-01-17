num = int(input())

phone_book = {} #phone_book = dict() (this can be used also)

for i in range(0, num):
    name, number = input().split()
    phone_book[name] = number

for j in range(0, num):
    name = str(input())

    if name in phone_book:
        number = phone_book[name]
        print(name + "=" + str(number))
    else:
        print("Not found")
