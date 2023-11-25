a, b = 0, 1

# Display the first two terms
print(a, b, end=" ")

# Generate and display the next eighteen terms in the sequence
for _ in range(18):
    next_term = a + b
    print(next_term, end=" ")
    a, b = b, next_term

print()  # Add a newline after the sequence