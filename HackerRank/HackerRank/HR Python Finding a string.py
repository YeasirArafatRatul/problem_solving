def count_substring(string, sub_string):
    count = 0
    for n in range (len(string),0,-1):
        try :
            index_of_str = n - len(sub_string)
            if string[index_of_str:n] == sub_string:
                count +=1
        except IndexError : break
    return count
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
