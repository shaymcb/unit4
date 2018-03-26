#Shaylee McBride
#26Mar2018
#stringUnion.py - prints all the letters in at least one word

def stringUnion(word1,word2):
    words = word1.lower() + word2.lower()
    combined = ''
    for ch in words:
        if ch not in combined:
            combined = combined + ch
    return combined
    
print(stringUnion('Pennsylvania','Mississippi'))
