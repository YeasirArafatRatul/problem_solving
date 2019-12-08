'''
@author "Yeasir Arafat Ratul"
'''




reversed_letters = {
  'A' : 'A',
  'E' : '3',
  'H' : 'H',
  'I' : 'I', 
  'J' : 'L',
  'L' : 'J',
  'M' : 'M',
  'O' : 'O',
  'S' : '2', 
  'T' : 'T',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X', 
  'Y' : 'Y',
  'Z' : '5',
  '1' : '1',
  '2' : 'S',
  '3' : 'E', 
  '5' : 'Z',
  '8' : '8'
}

def palindrome(string):
    reversed_string = string[::-1]
    is_mirrored = False
    is_palindrome = False
    mirrored_string = ""
    if string == reversed_string:
        is_palindrome = True
        
    for char in string[::-1]:
        if char in reversed_letters:
            mirrored_string += reversed_letters[char]
        if string == mirrored_string:
            is_mirrored = True
        else:
            is_mirrored = False
    #print(is_mirrored)

    
    if (not is_palindrome and is_mirrored==False):
        return "is not a palindrome"
    elif (not is_mirrored and is_palindrome):
        return "is a regular palindrome"
    elif (not is_palindrome and is_mirrored):
        return "is a mirrored string"
    else:
        return "is a mirrored palindrome"



if __name__ == "__main__":
    while True:
        try:
            string = input()
            print(f"{string} -- {palindrome(string)}.\n")
        except EOFError:
            break



