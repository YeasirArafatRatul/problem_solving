def dist(sx,sy,ex,ey):
    if sx == 0 and sy == 0 and ex == 0 and ey == 0:
        return ('')
    if (sx == ex):
        return abs(sy-ey)
    if (sx > ex):
        return dist(ex,ey,sx,sy)
    if (ex-sx <= ey-sy):
        return (ex-sx) + (ey-sy)

    sx += ey-sy
    ret = (ey-sy)*2

    if(sx%2 != ex%2):
        if((sx+ey)%2)!= 0:
            ret += 3
        else:
            ret += 1    
        sx += 1

    ret += (ex-sx)*2
    return ret



if __name__ == "__main__":
    for _ in range(4):
        sx,sy,ex,ey = map(int, input().split())
        print(dist(sx,sy,ex,ey))
