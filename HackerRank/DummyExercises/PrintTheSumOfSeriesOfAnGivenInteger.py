n = int(input("Enter a number: "))
result = 0
a = [ ] 

for i in range(1, n+1,1):
	print(i, sep=" ", end = " ") 
	result = result+i 
	if (i < n):
		print("+",sep = " ",end = " ")
		a.append(i) 
print("=",result)