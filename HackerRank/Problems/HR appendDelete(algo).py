"""
    for i in range(len(s)):
        s = s.replace(i,'')
        ops += 1
"""
# Complete the appendAndDelete function below.
def appendAndDelete(s,t,k):
    if len(s) <= len(t):
        string = ''
        ops = 0
        small_str = min(len(s),len(t))
        for i in range(small_str):
            if s[i] != t[i]:
                break
            else:
                string += s[i]

        sliced_s = s[len(string):len(s)+1]
            #print(sliced_s)
        sliced_t = t[len(string):len(t)+1]
            #print(sliced_t)
        ops = len(sliced_s)
            #print(ops)


        for j in range(len(sliced_t)):
            string += sliced_t[j]
            ops +=1
            #print(ops)

        if ops <= k:
            print("Yes")
        else:
            print("No")
    else:
        print("No")







