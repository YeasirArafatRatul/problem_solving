a = (3,4,5,6,7)
b = (4,5,6,7,8)

for i in range(min(len(a),len(b))):
    result = a[i]+b[i]
    print(result)


print(list(map(lambda x,y: x+y,a,b)))
