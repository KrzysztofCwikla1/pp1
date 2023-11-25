def has_negative_number(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

# main program
print(f"f(11, 6, -4) returns {has_negative_number(11, 6, -4)}")  # True
print(f"f(5, 4, 14) returns {has_negative_number(5, 4, 14)}")    # False