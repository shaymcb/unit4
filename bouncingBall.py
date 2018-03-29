#Shaylee McBride
#29Mar2018
#bouncingBall.py

from ggame import *

#Contants
XBOUND = 500
YBOUND = 1000

def moveBall():
    ball.x += data['xspeed']
    ball.y += data['yspeed']
    if ball.x == XBOUND or ball.x == 0:
        ybounce()
    if ball.y == YBOUND or ball.y == 0:
        xbounce()
    
def ybounce():
    data['yspeed'] = -1 * data['yspeed']

def xbounce():
    data['xspeed'] = -1 * data['xspeed']

if __name__ == '__main__':
    data = {}
    data['xspeed'] = 2
    data['yspeed'] = 2
    
    #shapes
    ballShape = CircleAsset(25,LineStyle(0,Color(0x000000,1)),Color(0x0000FF,1))
    rectangle = RectangleAsset(XBOUND-100,YBOUND-100,LineStyle(1,Color(0x000000,1),Color(0xFFFFFF,1)))
    
    ball=Sprite(ballShape)
    Sprite(rectangle,(100,100))
    
    App().run(moveBall)

    