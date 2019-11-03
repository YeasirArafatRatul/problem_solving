from math import atan,atan2
from math import degrees

ab = int(input())
bc = int(input())
#method atan() returns the arc tangent of x, in radians. and degree converts the radian
#tan0 = perpendicular/floor
#and a right triangle is divided into two equal tringle by its median
calc = degrees(atan((ab / 2) / (bc / 2)))

#"""atan2() returns atan(y / x), in radians
#calc2 = degrees(atan2(ab,bc))
result = round(calc)
#result2 = round(calc2)
print(str(result) + "°")
#print(str(result2) + "°")
