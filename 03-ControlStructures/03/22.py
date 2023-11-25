name = input("Enter a name: ")

# Check if the name is likely to be a female name
if name.lower().endswith("a"):
    print("The entered name '{}' is likely a female name in Polish.".format(name))
else:
    print("The entered name '{}' may not be a female name in Polish.".format(name))