x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# Determine the quadrant or axis
if x == 0 and y == 0:
    print("The point is at the origin (0,0).")
elif x == 0:
    print("The point is on the y-axis.")
elif y == 0:
    print("The point is on the x-axis.")
else:
    if x > 0:
        if y > 0:
            print("The point is in the first quadrant.")
        else:
            print("The point is in the fourth quadrant.")
    else:
        if y > 0:
            print("The point is in the second quadrant.")
        else:
            print("The point is in the third quadrant.")