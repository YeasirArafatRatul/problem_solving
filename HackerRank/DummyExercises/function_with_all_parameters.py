def functionWithAllParameters(name, *args, last_name='unknwon', **kwargs):
    print("name:" + name)
    print(args) #("args:" + args) if we print like that it becomes an tuple and raises error
    print("last name:" + last_name)
    print(kwargs)


functionWithAllParameters('yeasir', 2, 4, 4, a=4, b=5)

# parameters
# *args
# default parameters
# **kwargs
