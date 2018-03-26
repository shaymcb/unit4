#Shaylee McBride
#26Mar2018
#warmup11.py - primes

def prime(num):
    i = 2
    divisors = 0
    while i < num:
        if num%i == 0:
            num = num/i
            divisors += 1
        i += 1
    return(divisors == 0)

print(prime(5))
