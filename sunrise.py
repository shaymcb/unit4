#Shaylee McBride
#30Mar2018
#sunrise.py

from ggame import *

#constants
SCREENWIDTH = 1000
SCREENHEIGHT = 700

def rise():
    sun.y -= 0.5
    

if __name__ == '__main__':
    data = {}
    data['skyred'] = '00'
    data['skygreen'] = '00'
    data['skyblue'] = '00'
    data['skycolor']='0x'+data['skyred']+data['skygreen']+data['skyblue']
    
    groundBox = RectangleAsset(SCREENWIDTH, 200, LineStyle(0,Color(0x000000,1)),Color(0x006600,1))
    skyBox = RectangleAsset(SCREENWIDTH,SCREENHEIGHT,LineStyle(0,Color(0x000000,1)),Color(data['skycolor'],1))
    sunShape = CircleAsset(100,LineStyle(0,Color(0x000000,1)),Color(0xFFFF00,1))
    
    sky = Sprite(skyBox)
    sun = Sprite(sunShape,(SCREENWIDTH/2-100,SCREENHEIGHT-150))
    Sprite(groundBox, (0,SCREENHEIGHT-200))
    
    App().run(rise)
    
