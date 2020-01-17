def decorator(func):
    def square_func(a,b):
        x = a**2
        y = b**2
        value = func(x,y)
        return value
    return square_func
@decorator
def function(a,b):
    return a+b


if __name__ == "__main__":
    first_num = int(input())
    second_num = int(input())
    print(function(first_num,second_num))
