def celcius_to_fahrenheit(temp_in_celcius):
    temp = (temp_in_celcius*1.8)+32
    return temp


list_of_temp = [20,22,24,32,35,28,30]

for i in list_of_temp:
    print(type(i))
    print(celcius_to_fahrenheit(i))



print(list(map(celcius_to_fahrenheit,list_of_temp)))


print(list(map(lambda x: (x*1.8)+32, list_of_temp)))
