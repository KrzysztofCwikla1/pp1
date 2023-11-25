ean_13 = input("Enter the EAN-13 number: ")

# Check if the entered number is exactly 13 digits
if len(ean_13) == 13 and ean_13.isdigit():
    # Check if the first 3 digits are 590, indicating goods manufactured in Poland
    if ean_13[:3] == "590":
        print("The entered EAN-13 number is correct, and the product was manufactured in Poland.")
    else:
        print("The entered EAN-13 number is correct, but the product was not manufactured in Poland.")
else:
    print("Invalid EAN-13 number. Please enter a 13-digit numeric code.")