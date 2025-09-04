def sum_natural(n):
    s = 0
    i = 1
    while i <= n:
        s += i
        i += 1
    return s
print(sum_natural(10))
