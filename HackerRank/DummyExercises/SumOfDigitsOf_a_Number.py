n = int(input("Enter an integer number: "))
add = 0 
while(n>0):
	a = n%10
	add = a + add
	n= n //10 
	
print("Sum of the digits: ",add)
	