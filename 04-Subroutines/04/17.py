def sum_of_divisible_numbers(x, y):
    return sum(i for i in range(x, y+1) if i % 2 == 0 and i % 3 == 0 and i % 4 != 0)

# main program
range1 = (1, 20)
range2 = (10, 30)

print(f"f{range1} returns {sum_of_divisible_numbers(*range1)}")  # 24
print(f"f{range2} returns {sum_of_divisible_numbers(*range2)}")  # 48