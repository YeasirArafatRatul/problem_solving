def outer(expression):
    def decorator(function):
        def inner():
            a = function() + expression
            return a
        return inner
    return decorator

@outer("Ratul")
def greetings():
    return "good morning "

print(greetings())
