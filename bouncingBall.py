#Shaylee McBride
#29Mar2018
#bouncingBall.py

from ggame import *

#Contants
XBOUND = 950
YBOUND = 500
OFFSET = 50

def moveBall():
    ball.x += data['xspeed']
    ball.y += data['yspeed']
    if ball.x >= XBOUND - 50 or ball.x <= OFFSET:
        xbounce()
    if ball.y >= YBOUND - 50 or ball.y <= OFFSET:
        ybounce()
    
def ybounce():
    data['yspeed'] = -1 * data['yspeed']

def xbounce():
    data['xspeed'] = -1 * data['xspeed']

if __name__ == '__main__':
    data = {}
    data['xspeed'] = 3
    data['yspeed'] = 4
    
    #shapes
    ballShape = CircleAsset(25,LineStyle(0,Color(0x000000,1)),Color(0x0000FF,1))
    rectangle = RectangleAsset(XBOUND-OFFSET,YBOUND-OFFSET,LineStyle(1,Color(0x000000,1)),Color(0xFFFFFF,1))
    
    Sprite(rectangle,(OFFSET,OFFSET))
    ball=Sprite(ballShape,(OFFSET,OFFSET))
    
    App().run(moveBall)

    