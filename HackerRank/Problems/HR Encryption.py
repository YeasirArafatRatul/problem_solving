import math

def encryption(string,celling,floor):
    for i in range(celling):
        row = string[i::celling]
        print(row,sep=" ",end=" ")
        
          
    



  
if __name__ == "__main__":
        
    raw_string = input().strip()
    string = raw_string.replace(" ","")

    l = len(string)
    root = math.sqrt(l)

    celling = math.ceil(root)
    floor = math.floor(root)

    encryption(string,celling,floor)

