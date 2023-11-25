personal_data = "Mr. John May, born on 1998-02-16"

# Extract name and birthdate using slicing
name_start = personal_data.find(" ") + 1
name_end = personal_data.find(",")

birthdate_start = personal_data.find("on ") + 3

name = personal_data[name_start:name_end].strip()
birthdate = personal_data[birthdate_start:]

# Split the name into title, first name, and last name
title, first_name, last_name = name.split(" ")

# Display the information
print("Name:", first_name)
print("Surname:", last_name)
print("Initials:", f"{first_name[0]}.{last_name[0]}.")
print("Date of Birth:", birthdate)