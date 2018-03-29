#Shaylee McBride
#29Mar2018
#recursionDemo.py - recursive version of countdown()

def countdownr(n):
    if n == 0:  #base case
        print('BOOM')
    else:
        print(n)
        countdownr(n-1)  #aaah inception

countdownr(5)