def staircase(n):
    for i in range(1,n+1):
        #print the #, i times. so it will increase with each iteration
        print(('#'*i).rjust(n,' '))
        
        

n = int(input())
staircase(n)


# str.rjust(width[, fillchar])

#Parameters

# width − This is the string length in total after padding.

# fillchar − This is the filler character, default is a space.
