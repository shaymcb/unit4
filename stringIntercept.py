#Shaylee McBride
#26Mar2018
#stringIntercept.py - where do the strings overlap?

def stringIntercept(word1,word2):
    word1 = word1.lower()
    word2 = word2.lower()
    combined = ''
    for ch in word1:
        if ch in word2 and ch not in combined:
            combined = combined + ch
    return combined

print(stringIntercept('Mississippi','Pennsylvania'))
