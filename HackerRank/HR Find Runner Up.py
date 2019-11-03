
n = int(input())
array = list(map(int, input().split()))

largest = max(array)

for i in range(n):
    if largest == max(array):
        array.remove(max(array))

print(max(array))
