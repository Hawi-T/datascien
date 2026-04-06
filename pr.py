def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Check for divisors from 2 up to the square root of n
    # We use n**0.5 for efficiency
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If divisible, it's not prime
            
    return True  # If no divisors found, it is prime

# Testing the function
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")