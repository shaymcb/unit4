#Shaylee McBride
#22Mar2018
#monkeyBanana.py - the best game ever

from ggame import *
from random import randint

#constants
ROWS = 26  #all caps for constants
COLS = 50
CELL_SIZE = 20

#moves monkey right one cell if possible
def moveRight(event):
    if monkey.x < ((COLS-1)*CELL_SIZE):
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            
#moves monkey left one cell if possible
def moveLeft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            
#moves monkey up one cell if possible        
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            
#moves monkey down one cell if possible
def moveDown(event):
    if monkey.y < ((ROWS-1)*CELL_SIZE):
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves banana to random location and resets timer
def moveBanana():
    data['frames'] = 0
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE

#increases score and displays new text at bottom of screen
def updateScore():
    data['score'] += 10
    data['scoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))

#keeps track of how many frames have happened and moves banana if if 
#has been more than a random number between 50 and 300 (exciting!!)
def step():
    data['frames'] += 1
    if data['frames'] == randint(50,300):
        moveBanana()

#sets up and runs the game
if __name__ == '__main__':
    
    #hold variables in dictionary
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    #colors
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    #graphics
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(2,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(2,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(2,green),yellow)
    scoreBox = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,(CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().run(step)
