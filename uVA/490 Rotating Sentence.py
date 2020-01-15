strings = []

while True:
    try:
        strings.append(input())
    except EOFError:
        break


long_line = max(map(len,strings))



new_list = []
for i in range(long_line):
    new_list.append('')


strings.reverse()

for string in strings:
    #for each string add each character as a single element
    #in second or next iterations the value will be updated by index value
    
    for index, char in enumerate(string):
        new_list[index] += char

    # Add " " empty char to the rest of the places of smaller strings
    #to avoid index error
    for c in range(len(string), long_line):
        new_list[c] += " "

print("\n".join(map(str, new_list)))

