print("PROGRAM FOR ODD NUMBERS")
lower = int(input("Enter lower Limit: "))
upper = int(input("Enter upper limit: "))

for i in range(lower, upper):
	if i%2 == 1:
		print(i)