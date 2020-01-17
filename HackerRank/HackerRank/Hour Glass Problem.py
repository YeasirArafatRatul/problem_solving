# Python3 code fo hour glass pattern

rows_no = int(input("Enter no of rows:"))

def pattern(rows_no):                    # Function definition
    for i in range(1,rows_no+1):           # for loop for printing upper half
        for k in range(1,i,1):           # printing i spaces at the
            print(" ", end = "")         # beginning of each row
        for j in range(i,rows_no+1,1):     # printing i to rows value
            print(j, end = " ")          # at the end of each row
        print(" ")

    for i in range(rows_no-1,0,-1):        # for loop for printing lower half
        for k in range(1,i,1):           # printing i spaces at the
            print(" ", end = "")         # beginning of each row
        for j in range(i,rows_no+1,1):     # printing i to rows value
            print(j, end = " ")          # at the end of each row
        print(" ")
        
pattern(rows_no)
