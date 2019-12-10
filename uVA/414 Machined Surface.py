'''
@author
Yeasir Arafat Ratul
Daffodil Institute of Information and Technology [DIIT]

'''


while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            surface = []
            for i in range(n):
                stirng = str(input())
                no_of_X = stirng.count('X')
                surface.append(no_of_X)

        result = 0
        maximum = max(surface)
        for data in surface:
            result += maximum - data
        print(result)

    except EOFError:
        break
            

        
