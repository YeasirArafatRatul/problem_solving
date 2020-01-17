print("IDENTITY MATRIX")

n = int(input("Enter a number: "))

for i in range(1,n+1):
	for j in range(1,n+1):
		if(i==j):
			print("1")
		else:
			print("0")