#Shaylee McBride
#9Mar2018
#printnStars.py

def printnStars(n):
    i = 1
    while i < n:
        print(' '*(n-i)+'*'*(2*i-1))
        i += 1

printnStars(7)