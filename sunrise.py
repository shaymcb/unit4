#Shaylee McBride
#30Mar2018
#sunrise.py

from ggame import *

#constants
SCREENWIDTH = 1000
SCREENHEIGHT = 700

def rise():
    sun.y -= 0.5
    
def redden():
    data['skycolor'] = int(data['skyColor']) + 20000
    if data['skycolor'] < 100000:
        data['skycolor'] = '0'+str(data(skyColor))
    skyBox = RectangleAsset(SCREENWIDTH,SCREENHEIGHT,LineStyle(0,Color(0x000000,1)),Color('0x'+str(data['skycolor']),1))
    Sprite(skyBox)

if __name__ == '__main__':
    data = {}
    data['skycolor']='000000'
    
    groundBox = RectangleAsset(SCREENWIDTH, 200, LineStyle(0,Color(0x000000,1)),Color(0x006600,1))
    skyBox = RectangleAsset(SCREENWIDTH,SCREENHEIGHT,LineStyle(0,Color(0x000000,1)),Color('0x'+data['skycolor'],1))
    sunShape = CircleAsset(100,LineStyle(0,Color(0x000000,1)),Color(0xFFFF00,1))
    
    sky = Sprite(skyBox)
    sun = Sprite(sunShape,(SCREENWIDTH/2-100,SCREENHEIGHT-150))
    Sprite(groundBox, (0,SCREENHEIGHT-200))
    
    App().run(redden)
    
