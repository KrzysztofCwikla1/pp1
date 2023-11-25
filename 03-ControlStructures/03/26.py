car_speed = float(input("Enter the car speed in km/h: "))
speed_limit_min = 40
speed_limit_max = 140

# Check if the car speed exceeds the specified limits
if car_speed < speed_limit_min:
    print("Warning: The car speed is below the minimum limit of {} km/h.".format(speed_limit_min))
elif car_speed > speed_limit_max:
    print("Warning: The car speed exceeds the maximum limit of {} km/h.".format(speed_limit_max))
else:
    print("The car speed is within the allowed limits.")