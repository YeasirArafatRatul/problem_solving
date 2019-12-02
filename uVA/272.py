
signal = True
while True:
    try:
        dataset = []
        string = str(input())
        for i in string:
            if i == '"':
                if signal:
                    dataset.append('``')
                    
                else:
                    dataset.append("''")
                #for every closing quotation we need to make the signal = False 
                signal = not signal
            else:
                dataset.append(i)

        print(''.join(dataset))
    except EOFError:
        break
