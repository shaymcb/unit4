#Shaylee McBride
#9Mar2018
#colorChangeWindow.py

from ggame import *
from random import randint

outline = LineStyle(0,Color(0x000000,1)

def mouseClick(event):
    color = '0x'
    for i in range(6):
        rand = randint(0,9)
        rand = str(rand)
        color = color+rand
    
    background = RectangleAsset(600,1200,outline,color)
    Sprite(background)
