def calculate_arithmetic_operation(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        return None

# main program
num1, num2 = 2, 3

result_addition = calculate_arithmetic_operation(num1, num2, '+')
result_modulo = calculate_arithmetic_operation(num1, num2, '%')
result_exponentiation = calculate_arithmetic_operation(num1, num2, '**')
result_multiplication = calculate_arithmetic_operation(num1, num2, '*')
result_subtraction = calculate_arithmetic_operation(num1, num2, '-')

print(f"f({num1}, {num2}, '+') returns {result_addition}")
print(f"f({num1}, {num2}, '%') returns {result_modulo}")
print(f"f({num1}, {num2}, '**') returns {result_exponentiation}")
print(f"f({num1}, {num2}, '*') returns {result_multiplication}")
print(f"f({num1}, {num2}, '-') returns {result_subtraction}")