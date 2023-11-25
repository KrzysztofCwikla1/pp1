def generate_number_string(n):
    return ''.join(str(i) for i in range(1, n+1))

# main program
n1 = 11
n2 = 4

print(f"f({n1}) returns {generate_number_string(n1)}")  # "1234567891011"
print(f"f({n2}) returns {generate_number_string(n2)}")  # "1234"