def sum_of_repeated_digits(number):
    digit_str = str(number)
    repeated_digit_sum = 0

    for digit in digit_str:
        if digit_str.count(digit) > 1:
            repeated_digit_sum += int(digit)

    return repeated_digit_sum

# main program
num1 = 1027
num2 = 2333355
num3 = 513553007

print(f"f({num1}) returns {sum_of_repeated_digits(num1)}")  # 0
print(f"f({num2}) returns {sum_of_repeated_digits(num2)}")  # 9
print(f"f({num3}) returns {sum_of_repeated_digits(num3)}")  # 21