# factorial_calculator_recursive.py
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# main program
n = 5
print(f"f({n}) returns {factorial(n)}")  # 120