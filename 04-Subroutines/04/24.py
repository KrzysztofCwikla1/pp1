def calculate_expression(expression):
    result = 0
    current_number = 0
    operator = 1  # 1 for addition, -1 for subtraction

    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '+':
            result += operator * current_number
            current_number = 0
            operator = 1
        elif char == '-':
            result += operator * current_number
            current_number = 0
            operator = -1

    # Add the last number in the expression
    result += operator * current_number

    return result

# Example usage:
expression1 = "2+3"
expression2 = "3+8+1"
expression3 = "2+3-4+5-0"

result1 = calculate_expression(expression1)
result2 = calculate_expression(expression2)
result3 = calculate_expression(expression3)

print(f"f(\"{expression1}\") returns {result1}")  # 5
print(f"f(\"{expression2}\") returns {result2}")  # 12
print(f"f(\"{expression3}\") returns {result3}") 