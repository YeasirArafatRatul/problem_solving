
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def bubble_sort(a):
    count = 0
    for num in range(len(a)):
        for j in range(1,len(a)):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]
                count += 1
    return count

print(f"Array is sorted in {bubble_sort(a)} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
