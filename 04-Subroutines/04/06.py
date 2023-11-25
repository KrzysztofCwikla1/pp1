def count_negative_even_numbers(x, y):
    return sum(1 for i in range(x, y+1) if i < 0 and i % 2 == 0)

# main program
range1 = (-7, 8)
range2 = (-1, 11)

print(f"f{range1} returns {count_negative_even_numbers(*range1)}")  # 3
print(f"f{range2} returns {count_negative_even_numbers(*range2)}")  # 0