first = True
while True:
    try:
        dataset = []
        string = str(input())
        for i in string:
            if i == '"':
                if first:
                    dataset.append('``')
                    #dataset.append('`')
                else:
                    dataset.append("''")
                    #dataset.append("'")
                first = not first
            else:
                dataset.append(i)

        print(''.join(dataset))
    except EOFError:
        break
