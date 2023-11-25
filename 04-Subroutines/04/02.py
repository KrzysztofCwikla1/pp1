def is_in_range(number, x, y):
    return x <= number <= y

# main program
user_number = int(input("A number: "))
range_start = 2
range_end = 15

if is_in_range(user_number, range_start, range_end):
    print(f"Number {user_number} in the range <{range_start},{range_end}>: yes")
else:
    print(f"Number {user_number} is not in the range <{range_start},{range_end}>.")