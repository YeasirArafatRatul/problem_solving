def fibWord(n): 
    Sn_1 = "0"
    Sn = "01"
    tmp = "" 
    for i in range(2, n + 1): 
        tmp = Sn 
        Sn += Sn_1 
        Sn_1 = tmp 
    return Sn 
  
# driver program 
n = 6
print (fibWord(n)) 
