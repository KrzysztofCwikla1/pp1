rows = 7
columns = 7

# Display the lottery coupon
for row in range(1, rows + 1):
    for col in range(row, row + columns * (rows - 1) + 1, rows):
        print("{:2d}".format(col), end=" ")
    print()  # Move to the next line after each row