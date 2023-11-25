human_years = int(input("Enter the dog's age in human years: "))

# Calculate the dog's age in dog years
if human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4

# Display the result
print("The dog's age in dog years is:", dog_years)