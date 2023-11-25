sum_numbers = 0
count_numbers = 0
i=01
# Get input from the user
while True:
    number = float(input("Enter a number (enter 0 to finish)")) 
    
    # Check if the user wants to finish entering numbers
    if number == 0:
        break

    # Update sum and count
    sum_numbers += number
    count_numbers += 1
    i+=1
# Calculate arithmetic mean
if count_numbers == 0:
    print("No numbers entered.")
else:
    mean = sum_numbers / count_numbers
    print(f'quantity: {i}')
    print("\nSum: {:.2f}".format(sum_numbers))
    print("Arithmetic Mean: {:.2f}".format(mean))