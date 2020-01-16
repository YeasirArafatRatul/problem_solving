
vowels = set(list("aeiouAEIOU"))
while True:
    try:
        line = input()
        encrypted_msg = ''

        i = char_index = 0
        while i < len(line):
            if not line[i].isalpha():
                encrypted_msg += line[i]
                i +=1
            else:
                char_index = i
                while char_index < len(line) and line[char_index].isalpha():
                       char_index += 1
                word = line[i:char_index]
                if word[0] in vowels:
                    encrypted_msg += (word + "ay")
                else:
                    encrypted_msg += (word[1:] + word[0] + "ay")
                i = char_index
        print(encrypted_msg)
    except EOFError:
           break


    
