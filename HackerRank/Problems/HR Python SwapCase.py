def swap_case(s):
    string = ''
    for item in s:
        if item.islower():
            string += item.upper()
        elif item.isupper():
            string += item.lower()
        elif ' ':
            string += item
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
