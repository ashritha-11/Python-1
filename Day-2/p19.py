#program to print all prime numbers between 1 to n
def prime_numbers(n):
    for num in range(2, n+1):   
        is_prime = True
        for i in range(2, num): 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
prime_numbers(20)
