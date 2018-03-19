#Shaylee McBride
#19March2018
#printSquares.py

def printSquares(rows,columns):
    for i in range(columns):
        print("+--"*rows+'+')
        print("|  "*(rows+1))
    print("+--"*rows+'+')

printSquares(3,5)
