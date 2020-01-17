def another(func):
    print(func.__name__)
    def wrapper():
        print("fuck")
        return func()
    return wrapper

def decorator(func):
    print(func.__name__)
    def result():
        print("decorator executed.")
        return func()
    
    return result

@another
@decorator
def functions():
    print("decorated with decorator")        

functions()

#print(functions.__name__)
#print(type(functions))
