#Shaylee McBride
#28Mar2018
#multiply.py - teach yo kids to math

from random import randint

def encourage():
    selection = randint(1,10)
    if selection == 1:
        return "Keep it up!"
    elif selection == 2:
        return "You got this!"
    elif selection == 3:
        return "Nerd."
    elif selection == 4:
        return "Nice!"
    elif selection == 5:
        return "Genius!"
    elif selection == 6:
        return "HOLY CAT HAIR BRO THIS IS THE FURTHEST ANYONE HAS EVER GOTTEN!!!!"
    elif selection == 7:
        return "You slay, hey, all day, okay, you slay, okay, you slay, okay, you gon slay, slay"
    elif selection == 8:
        return "Are you going on a trip in your favorite rocket ship? Cuz you're a Little Einstein!"
    elif selection == 9:
        return "good job i guess"
    else:
        return "Yeet"

if __name__ == "__main__":
    numberCorrect = 0
    while True:
        num1 = randint(1,12)
        num2 = randint(1,12)
        print(num1,'+',num2,"=")
        answer = float(input('?'))
        elif num1 + num2 != answer:
            print("Sorry, incorrect.")
        else:
            numberCorrect += 1
            if numberCorrect%5 = 0:
                encourage()

