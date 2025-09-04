#sum of digits
def sum(n):
    s = 0
    while n > 0:
        digit = n % 10   
        s += digit
        n //= 10       
    return s
print(sum(123))
