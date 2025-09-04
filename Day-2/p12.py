def firstLast(n):
    last = n % 10         
    while n >= 10:        
        n //= 10
    first = n
    return first, last
print(firstLast(123))
