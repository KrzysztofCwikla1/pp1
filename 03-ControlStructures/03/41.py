correct_pin = "0805"

# Initialize attempts counter
attempts = 0

# Allow three attempts
while attempts < 3:
    # Get input from the user
    entered_pin = input("Enter the PIN code: ")

    # Check if the entered PIN is correct
    if entered_pin == correct_pin:
        print("PIN is correct. Access granted.")
        break
    else:
        attempts += 1
        remaining_attempts = 3 - attempts
        print("Incorrect PIN. {} attempts remaining.".format(remaining_attempts))

# Check if the card is blocked
if attempts == 3:
    print("Card is blocked. Contact customer support.")