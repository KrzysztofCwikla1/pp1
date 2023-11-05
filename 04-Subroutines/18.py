def numbers(n):
    string=""
    for i in range(1,n+1):
        string += f"{i},"
    return string.strip()
print(f"Numbers <1,15>: {numbers(15)}")
print(f"Numbers <1,7>: {numbers(7)}")

