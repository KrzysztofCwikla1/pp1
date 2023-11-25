def digit_sum(number, even):
    digit_sum = 0

    for digit in str(number):
        d = int(digit)
        if even and d % 2 == 0:
            digit_sum += d
        elif not even and d % 2 != 0:
            digit_sum += d

    return digit_sum
number1 = 3124
number2 = 20576
number3 = 13115

print(f"digit_sum({number1}, True) returns {digit_sum(number1, True)}")  # Sum of even digits: 6
print(f"digit_sum({number1}, False) returns {digit_sum(number1, False)}")  # Sum of odd digits: 4

print(f"digit_sum({number2}, True) returns {digit_sum(number2, True)}")  # Sum of even digits: 8
print(f"digit_sum({number2}, False) returns {digit_sum(number2, False)}")  # Sum of odd digits: 12

print(f"digit_sum({number3}, True) returns {digit_sum(number3, True)}")  # Sum of even digits: 0
print(f"digit_sum({number3}, False) returns {digit_sum(number3, False)}")  # Sum of odd digits: 10
