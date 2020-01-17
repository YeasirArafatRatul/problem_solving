# import module sys to get the type of exception
import sys

randomList = ['a', 4, 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        ent = int(entry)
        r = 1/ent
        print("The result:",entry,"is",r,"\n")
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()

