number = int(input("Enter a number to generate its multiplication table: "))

# Display the multiplication table
print("\nMultiplication Table for", number)
print("-------------------------------")
for i in range(1, 11):
    result = number * i
    print("{:2d} x {:2d} = {:2d}".format(number, i, result))