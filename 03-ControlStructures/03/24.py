current_price = int(input("Enter the current price of the product: "))
previous_price = int(input("Enter the previous price of the product: "))

# Calculate the percentage decrease
percentage_decrease = ((previous_price - current_price) / previous_price) * 100

# Check if the price has decreased by at least 10%
if percentage_decrease >= 10:
    print("Recommendation: Consider purchasing! The price has decreased by {:.2f}%.".format(percentage_decrease))
else:
    print("No recommendation at this time. The price has not decreased by at least 10%.")