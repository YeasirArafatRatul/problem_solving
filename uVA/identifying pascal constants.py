'''
while True:
    constant = input().strip()
    if constant != '*':
        try:
            if (constant.isnumeric())==True:
                if constant
                print(f'{constant} is legal')
            else:
                print(f'{constant} is illegal')
        except:
            print('error')
    else:
        break


a = '1.2,1.0e-55,1e-12 +4.1234567890E-9999,'

pattern = r'\+?\d*[eE]?\.?\-?\d*[eE]?\-?\d*'

'''

import re
expression_integer = r'^[-+]?(\d+)$'
expression_real = r'^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$'
while True:
    constant = input().strip()
    if constant == '*':
        break
    else:
        if re.search(expression_real,constant) and not re.search(expression_integer,constant):
            print(f'{constant} is legal.')
        else:
            print(f'{constant} is illegal.')
