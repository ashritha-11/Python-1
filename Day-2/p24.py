#prime factors of a number
def prime_factors(n):
    i = 2
    while i <= n:
        if n % i == 0:  
            print(i, end=" ")
            n //= i      
        else:
            i += 1
prime_factors(20)
