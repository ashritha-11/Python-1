def count(n):
    count = 0
    if n == 0:
        return 1   
    while n > 0:
        count += 1
        n //= 10
    return count
print(count(123))
