#a = range(1,100)

#print(list(map(lambda x:x**2,filter(lambda x:x%2==1,a))))

'''
def square(a):
    return a**2

def odd(x):
    if x%2==1:
        value = square(x)
        return value
    else:
        return ''
list1 = []
for i in range(1,100):
    a = odd(i)
    list1.append(a)
print(list1)

b = filter(lambda x:x%2==1,a)
print(b)
c = map(lambda x:x**2,b)
print(c)
print(list(c))
'''
import functools
# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: "%.3f" %(x**2), my_floats))
filter_result = list(filter(lambda name: len(name)<=7, my_names))
reduce_result = functools.reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
