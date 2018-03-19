#Shaylee McBride
#9Mar2018
#functionDemo.py - how to write our own functions

def hw():
    print('hello, world')
    
def double(thingToDouble):
    print(thingToDouble * 2)

def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)

def slope(x1, y1, x2, y2):
    print((y2-y1)/(x2-x1))

print('the max of 3 and 4 is',max(3,4))
print('the max of 3 and 4 is',bigger(3,4)) #need to use return, not print

"""
slope(1,-1,2,2)
slope(True,True,False,False) #sketchy

bigger(4,3)
bigger('hi','hoe you thought')
bigger(False,True)

double(12)
double('w')
double(True)
"""
