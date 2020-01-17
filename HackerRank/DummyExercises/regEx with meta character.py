import re

phone_numbers = "'01900000000','01700000000','01911111111','01811112222'"

find_numbers = re.findall('019........',phone_numbers)
print(find_numbers)
find_numbers = re.findall('019\w\w\w\w\w\w\w\w\w\w\w',phone_numbers)
