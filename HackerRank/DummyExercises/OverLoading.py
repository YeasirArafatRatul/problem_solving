class person:
    def __init__(R,name,age):
        R.name = name
        R.age = age
    def __str__(R):
        return("name: {}\nage: {}\n".format(R.name,R.age))

class teacher(person):
    def __init__(R,name,age,sub):
        person.__init__(R,name,age)
        R.sub = sub
    def __str__(R):
        return(person.__str__(R)+"sub: {}".format(R.sub))

class student(person):
    def __init__(R,name,age,roll):
        person.__init__(R,name,age)
        R.roll = roll
    def __str__(R):
        return(person.__str__(R)+"roll: {}".format(R.roll))
