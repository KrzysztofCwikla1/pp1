time_24h = input("Enter the time in 24-hour format (hh:mm): ")
try:
    hours, minutes = map(int, time_24h.split(':'))
except ValueError:
    print("Invalid input format. Please enter the time in hh:mm format.")
    exit()
if hours < 12: 
    am_pm= "AM" 
else:
    am_pm ="PM"
if hours % 12 != 0:
    hours_12= hours % 12
else:
    hours_12=12
time_12h = "{:02d}:{:02d} {}".format(hours_12, minutes, am_pm)
print("Time in 12-hour format: {}".format(time_12h))