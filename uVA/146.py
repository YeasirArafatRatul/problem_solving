while True:
    string = input()
    if string == '#':
        break
    successor = None
    inp = list(string)
    for i in range(len(inp)-1, 0, -1):
      #print(i)
      if ord(inp[i]) > ord(inp[i-1]):

        successor = ("".join(inp[0:i-1]) if i > 1 else "")
        #print(successor)
        
        min_v = inp[i]
        #print(min_v)
        min_i = i
        #print(min_i)
        #print(f"min_v = {min_v}, min_i = {min_i}")
        for j in range(i, len(inp)):
          #print(f'i = {i} and length of inp = {len(inp)}')
          if inp[j] < min_v and inp[j] > inp[i-1]:
            min_v = inp[j]
            min_i = j
            #print(f"min_v = {min_v} and min_i = {min_i}")
      
        successor += min_v
        #print("successor: = ",successor)
        inp[min_i] = inp[i-1]
        #print("min_i: " , inp[min_i])
        successor += "".join(sorted(inp[i:]))
        #print("successor: = ",successor)
        break

  #output
    if successor:
        print(f"{successor}")
    else:
        print("No Successor")

