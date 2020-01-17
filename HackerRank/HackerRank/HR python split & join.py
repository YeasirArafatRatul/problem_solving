#print('-'.join(input().split()))
def split_and_join(string):
    line = string.split()
    line =('-'.join(line))
    return(line)



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
