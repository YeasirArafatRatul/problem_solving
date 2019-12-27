#it_gives_the_output_but_someHow_is_not_accepted

def marvelous_maze(string):
        
    repeat = 0
    for s in string:
        if s.isnumeric():
            repeat += int(s)    
        elif s == 'b':
            for i in range(repeat):
                print(' ',end='')
            repeat = 0
        elif s == '!':
            print("")
        else:
            for i in range(repeat):
                print(s,end='')
            repeat = 0

string_list = [] 
while True:
    string = input()
    string_list.append(string)
    if string == "":
        for string in string_list:
            marvelous_maze(string)
            print()
        string_list = []
    
    

