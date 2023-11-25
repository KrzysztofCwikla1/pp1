def generate_asterisks(n):
    return '*/' * (n - 1) + '*' if n > 1 else '*'

# main program
n1 = 4
n2 = 2

print(f"f({n1}) returns {generate_asterisks(n1)}")  # "*/*/*/*"
print(f"f({n2}) returns {generate_asterisks(n2)}")  # "*"