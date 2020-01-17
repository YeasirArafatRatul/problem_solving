def phone_no_checker(phone_no):
    def decorator(function):
        def checker_function():
            operators_ip = ['017','018','019','016','015']
            if phone_no[0:3] not in operators_ip:
                return "Invalid Operator's ID"
            elif len(phone_no)>11 or len(phone_no)<11:
                return "Phone Number must contain 11 characters"
            else:
                print("Number Verified")
                return function()
        return checker_function()
    return decorator


@phone_no_checker("01900000000")
def registration():
    return "Your Number is Registered"


print(registration)
