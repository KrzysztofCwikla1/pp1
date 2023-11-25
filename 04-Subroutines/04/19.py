def is_valid_product_code(product_code):
    digit_sum = sum(int(digit) for digit in product_code[:-1])
    control_digit = int(product_code[-1])
    return digit_sum % 7 == control_digit

# main program
code1 = "1082"
code2 = "2035"
code3 = "1114"
code4 = "7071"

print(f"f(\"{code1}\") returns {is_valid_product_code(code1)}")  # True
print(f"f(\"{code2}\") returns {is_valid_product_code(code2)}")  # True
print(f"f(\"{code3}\") returns {is_valid_product_code(code3)}")  # False
print(f"f(\"{code4}\") returns {is_valid_product_code(code4)}")  # False