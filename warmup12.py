#Shaylee McBride
#29Mar2018
#warmup12.py - GCF

def GCF(num1,num2):
    i = min(num1,num2)
    while True:
        if num1%i==0 and num2%i==0:
            return i
        i -= 1
        

print(GCF(12,15))
print(GCF(5,9))
print(GCF(16,64))