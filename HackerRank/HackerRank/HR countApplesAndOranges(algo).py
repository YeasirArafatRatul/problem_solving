def countApplesAndOranges(s, t, a, b, apples, oranges):
    #print(b)
    apples_inside_home = 0
    oranges_inside_home = 0
    for i in apples:
        apples_distance = a + i
        #print(f"apples_distance{i} :",apples_distance)
        if apples_distance >= s and apples_distance <= t:
            apples_inside_home +=1
            
        

    for j in oranges:
        orange_distance = b + j
        #print(f"orange_distance{j} :",orange_distance)
        if orange_distance >= s and orange_distance <= t:
            oranges_inside_home += 1
            

    print(apples_inside_home,end="\n")
    print(oranges_inside_home)
    
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
