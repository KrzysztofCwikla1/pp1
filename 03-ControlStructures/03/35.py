for number in range(1, 31):
    output = ""

    # Check if the number is divisible by 3
    if number % 3 == 0:
        output += "THREE"

    # Check if the number is divisible by 5
    if number % 5 == 0:
        output += "FIVE"

    # Check if the number is divisible by both 3 and 5
    if output == "THREEFIVE":
        output = "BINGO"

    # Display the result
    if output:
        print(output)
    else:
        print(number)