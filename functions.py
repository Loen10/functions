# Conversion Calculator
# Logan Nance

# get user input for the length to convert
length = float(input("What is the length? "))
print(length)

# get the unit from the user
unit = input("What unit is the length? ")
print(unit)

# convert the input into the desired units
# to convert in to mm: in * 25.4
if unit == "in":
    converted_length = length * 25.4
    converted_unit = "mm"
elif unit == "mm":
    converted_length = length / 25.4
    converted_unit = "in"
else:
    print("Your unit sucks. Try again")

# output the answer to the user
print(converted_length, converted_unit)