#Shaylee McBride
#26Mar2018
#triangle.py - area of triangle!!

from math import sqrt 

def distance(x1,y1,x2,y2):
    d = sqrt((x1-x2)**2+(y1-y2)**2)
    return d

def fuckingHeron(a,b,c):
    s = 1/2 * (a+b+c)
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return round(area,3)
    

if __name__ == '__main__':  
    #inputs
    x1 = float(input('x1 = '))
    y1 = float(input('y1 = '))
    x2 = float(input('x2 = '))
    y2 = float(input('y2 = '))
    x3 = float(input('x3 = '))
    y3 = float(input('y3 = '))
    
    #distances:
    a = distance(x1,y1,x2,y2)
    b = distance(x2,y2,x3,y3)
    c = distance(x3,y3,x1,y1)
    
    print(fuckingHeron(a,b,c))
    