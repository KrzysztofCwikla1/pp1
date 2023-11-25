amount = int(input("Enter the amount in Polish Zlotys (PLN): "))

# Calculate the number of each type of coin
coins_5 = amount // 5
remainder = amount % 5
coins_2 = remainder // 2
coins_1 = remainder % 2

# Display the result
print("\nMinimum number of coins:")
print("5 PLN coins: {}".format(coins_5))
print("2 PLN coins: {}".format(coins_2))
print("1 PLN coins: {}".format(coins_1))