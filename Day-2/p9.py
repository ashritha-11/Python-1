#factorial of a number
def fact(n):
    while n>0:
        n=n*(n-1)
        return n
print(fact(6))
