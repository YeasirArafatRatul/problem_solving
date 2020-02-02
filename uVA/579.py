while True:
    hour,minutes = map(int,input().split(":"))
    if hour == 0 and minutes == 0:
        break

    degree_of_min = 0

    #6 degree differece for each minute 180degree/30min = 6
    for i in range(minutes):
        degree_of_min += 6

    degree = 0
    if hour < 12:
        for i in range(hour):
            degree += 30
        degree_of_hour = degree + (minutes*0.5)
    else:
        degree_of_hour = minutes*0.5
            

    degree = (degree_of_hour - degree_of_min if degree_of_hour > degree_of_min else degree_of_min - degree_of_hour)
    result = (degree if degree <= 180 else 360-degree)
    print("{:.3f}".format(result))
