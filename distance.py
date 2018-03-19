#Shaylee McBride
#19Mar2018
#distance.py - distance formula

from math import sqrt 

def distance(x1,y1,x2,y2):
    d = sqrt((x1-x2)**2+(y1-y2)**2)
    return d

print(distance(3,4,-5,2))
