def upper_d(func):
    print("I am upper_d")
    def inner():
        print("I am inner")
        str1 = func()
        return str1.upper()
    return inner

def split_d(func):
    print("I am split_d")
    def wrapper():
        print("I am wrapper")
        str2 = func()
        return str2.split()
    return wrapper


@split_d
@upper_d
def ordinary():
    return "I love You Orpeeta"

print(ordinary())
