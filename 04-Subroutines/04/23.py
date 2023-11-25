# power_calculator_recursive.py
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

# main program
x = 5
n = 3
print(f"f({x}, {n}) returns {power(x, n)}")  # 125