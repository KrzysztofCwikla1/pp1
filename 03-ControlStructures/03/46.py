import random

# Display 20 integer random numbers in the range of 5 to 10
for _ in range(20):
    random_number = random.randint(5, 10)
    print(random_number, end=" ")

print()  # Add a newline after the random numbers