a = int(input("Enter the length of the rectangle (a): "))
b = int(input("Enter the width of the rectangle (b): "))

# Display the rectangle
for i in range(a):
    if i == 0 or i == a - 1:
        print("*" * b)
    else:
        print("*" + " " * (b - 2) + "*")