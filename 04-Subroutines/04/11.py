def count_people_in_room(detector):
    count = 0
    max_count = 0

    for event in detector:
        if event == '+':
            count += 1
            max_count = max(max_count, count)
        elif event == '-':
            count -= 1

    return max_count >= 3

# main program
detector1 = "+-+++-+---"
detector2 = "+-+-+-+-"

print(f"f(\"{detector1}\") returns {count_people_in_room(detector1)}")  # True
print(f"f(\"{detector2}\") returns {count_people_in_room(detector2)}")  # False