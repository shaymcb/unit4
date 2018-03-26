#Shaylee McBride
#26Mar2018
#stringUnion.py - prints all the letters in at least one word

def stringUnion(word1,word2):
    combined = ''
    for ch in word1+word2:
        if ch not in combined:
            combined = combined + ch.lower()
    return combined
    
print(stringUnion('Pennsylvania','Mississippi'))
