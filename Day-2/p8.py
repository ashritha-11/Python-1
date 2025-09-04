#check whether prime number or not 
def is_prime(n):
    if n <= 1:
        return False  
    i = 2
    while i <= n // 2:   
        if n % i == 0:
            return False
        i += 1
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
