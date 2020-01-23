row,col = map(int,input().split())

puzzle = []

for i in range(col*row):
    data = str(input())
    if data == '0 0':
        break
    puzzle.append(data)


#left_top_corner = 'FOOF'
#right_top_corner = 'FFOI'
#left_bottom_corner = 'IOFF'
#right_bottom_corner = 'IFFI'


#top_row_middle = 'FOOI'
#middle_rows = 'IOOI'
#bottom_row_middle = 'IOFI'

LTC = puzzle.count('FOOF')
RTC = puzzle.count('FFOI')
LBC = puzzle.count('IOFF')
RBC = puzzle.count('IFFI')

TRM = puzzle.count('FOOI')
BRM = puzzle.count('IOFI')
LCM = puzzle.count('IOOF')
RCM = puzzle.count('IFOI')

MRC = puzzle.count('IOOI')

#print(LTC,RTC,LBC,RBC)
#print(TRM,BRM,LCM,RCM,MRC)

if row == 2 and col == 2:
    if LTC == 1 and RTC == 1 and LBC == 1 and RBC == 1:
        print("YES")
    else:
        print("NO")
        
elif row == 2 and col > 2:
    if LTC == 1 and RTC == 1 and LBC == 1 and RBC == 1 and TRM == col - 2 and BRM == col - 2:
        print("YES")
    else:
        print("NO")
        
    
elif col == 2 and row > 2:
    if LTC == 1 and RTC == 1 and LBC == 1 and RBC == 1 and LCM == row - 2 and RCM == row - 2:
        print("YES")
    else:
        print("NO")
        
elif (LTC == 1 and RTC == 1 and LBC == 1 and RBC == 1 and TRM == col-2 and BRM == col - 2
            and LCM == row - 2 and RCM == row - 2 and MRC == (col*row - (LTC+RTC+LBC+RBC+TRM+BRM+LCM+RCM))):
            print("YES")
    
else:
    print("NO")
