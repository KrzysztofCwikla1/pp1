num_products = int(input("Enter the number of products purchased: "))
product_price = float(input("Enter the price of each product: "))

# Calculate the total cost without discount
total_cost = num_products * product_price

# Check if the discount applies (25% discount for each product when purchasing more than two)
if num_products > 2:
    discount_amount = 0.25 * (num_products - 2) * product_price
    total_cost -= discount_amount

# Display the result
print(f"Total amount to be paid: ${total_cost:.2f}")