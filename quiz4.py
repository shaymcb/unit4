#Shaylee McBride
#2Apr2018
#quiz4.py

def count(num):
    for i in range(1,num+1):
        print(i)

def excitedPrint(string):
    print(string.upper()+'!!!')

def firstLetter(string):
    for ch in string:
        return(ch)

def repeats(first,second,third):
    if first == second or first == third or second == third:
        return True
    else:
        return False

count(4)
excitedPrint('death is inevitable')
print(firstLetter('forgetful'))
print(repeats(3,4,4))
print(repeats('four',4,'For'))