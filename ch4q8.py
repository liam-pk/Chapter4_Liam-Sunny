##Write a function area_of_circle(r) which returns the area
##of a circle of radius r.


import math
def areaofcircle (r):
    return math.pi*r**2

radius = int(input("What is the radius of your circle"))

print(areaofcircle(radius))