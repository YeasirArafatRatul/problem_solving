def counter(string):
    total = 0
    increament = 0
    for letter in string:
        if letter == 'O':
            increament += 1
            total += increament
            
        else:
            increament = 0
    return total

if __name__ == "__main__":
    n = int(input())
    strings = []
    for i in range(n):
        string = str(input())
        strings.append(string)
        print(counter(string))


