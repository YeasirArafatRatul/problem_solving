
while True:
    try:
        sentence = list(input().split(" "))
        reverse = []
        for i in sentence:
            reverse.append(i[::-1])
        print(*reverse)
    except:
        break
    
    
