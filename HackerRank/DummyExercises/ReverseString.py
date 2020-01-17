a = int(input())

reverse = 0 
while(a>0):
	modulas = a%10 
	reverse = reverse*10 + modulas 
	a = a//10 
print("reverse: ",reverse)