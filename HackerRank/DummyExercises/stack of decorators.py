'''
def first(func):
    print(f"{func.__name__}:  Pushed in stack")
    def inner_of_first():
        print(f"inner_of_first:  Pushed in stack")
        print("inner_of_first:  Executed and Popped")
        return func()
    return inner_of_first

def second(func):
    print(f"{func.__name__}:  Pushed in stack ")
    def inner_of_second():
        print(f"inner_of_second:  Executed and Popped ")
        return func()
    return inner_of_second


@first
@second
def general():
    print("general:  Executed and Popped")


general()
'''

def a():
    print("hello")

def b(func):
    print("ratul")

def c(func):
    print("boss")

c(b(a()))
    
