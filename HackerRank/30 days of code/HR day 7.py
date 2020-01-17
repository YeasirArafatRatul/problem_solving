input()

arr = str(input()).split(" ")
arr.reverse()

for num in arr:
#print(map(str,arr[::-1]))
    print(num + " ", end="")


#print(" ".join(map(str, arr[::-1])))  #comprehension
