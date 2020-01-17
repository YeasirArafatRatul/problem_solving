from math import sqrt

def first_decorator(func):
    print("I am first_decorator")
    def square(a,b):
        print("I am inner function of first_decorator")
        x = a**2
        y = b**2
        return func(x,y)
    return square

def second_decorator(func):
    print('Hello!\nI am second_decorator and I am executed first')
    def square_root(x,y):
        print("I am inner function of second_decorator")
        print(f"{x} + {y} = {x+y}")
        answer = sqrt(x+y)
        func(x,y)
        return answer
    return square_root


@second_decorator
@first_decorator
def function(a,b):
    return a,b 

print(function(3,4))


