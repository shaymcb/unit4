#Shaylee McBride
#19March2018
#returnDemo.py - how to use return

from random import randint

def randEven(low,high):
    n=randint(low,high)
    while n%2 != 0:
        n = randint(low,high)
    return(n)

print("your even numbers are",randEven(0,100),randEven(0,100),randEven(1,100))