creditcard_number = input("Enter a 16-digit credit card number: ")
formatted_number = f"{creditcard_number[:4]} {creditcard_number[4:8]} {creditcard_number[8:12]} {creditcard_number[12:]}"
print("Formatted Credit Card Number:", formatted_number)