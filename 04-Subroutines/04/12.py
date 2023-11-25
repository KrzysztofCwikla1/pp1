def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# main program
n1 = 5
n2 = 15

print(f"f({n1}) returns {fibonacci(n1)}")  # 3
print(f"f({n2}) returns {fibonacci(n2)}")  # 21