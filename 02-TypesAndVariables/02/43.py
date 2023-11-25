# Enter your name
name = input("Enter your name: ")

# Display numerical representation of each letter
print("Numerical representation of each letter in your name:")
for char in name:
    print(f"{char}: {ord(char)}")