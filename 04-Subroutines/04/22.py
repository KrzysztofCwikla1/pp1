# sum_of_natural_numbers_calculator_recursive.py
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n-1)

# main program
n = 10
print(f"f({n}) returns {sum_of_natural_numbers(n)}")  # 55