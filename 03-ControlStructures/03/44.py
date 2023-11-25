def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get input from the user
N = int(input("Enter the value of N: "))

# Find and display the first N prime numbers
count_primes = 0
num = 2  # Starting from the first prime number

while count_primes < N:
    if is_prime(num):
        print(num, end=" ")
        count_primes += 1
    num += 1

print()  # Add a newline after the prime numbers