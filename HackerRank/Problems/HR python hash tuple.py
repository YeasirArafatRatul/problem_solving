n = int(input())
lists = map(int, input().split())
t= tuple(lists)
hashed_tuple = hash(t)
print(hashed_tuple)


#print(input()==0 or hash(tuple(map(int,input().strip().split()))))
