# Conversion Calculator
# Logan Nance

def parse_length_with_unit(length_with_unit: str) -> float:
    (length, unit) = length_with_unit.split()
    length = float(length)

    # convert the input into the desired units
    # to convert in to mm: in * 25.4    
    while True:
        if unit == "in":
            converted_length = length * 25.4
            converted_unit = "mm"
            break
        elif unit == "mm":
            converted_length = length / 25.4
            converted_unit = "in"
            break
        else:
            print("Your unit sucks. Try again")
    
    return converted_length

# get user input for the length to convert
print(parse_length_with_unit(input("What is the length and unit? ")))