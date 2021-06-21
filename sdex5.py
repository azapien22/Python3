# More Variables & Printing
# Removed "my_"
# Inch to cm & lbs to kg conversion w/ variables
# Used Round() Function


name = "Amaury Zapien"

age = 35 # not a lie

height = 74 # inches

weight = 180 # lbs

eyes = 'Blue'

teeth = 'white'

hair = 'brown'

print(f"let's talk about {name}.")

print(f"He's {height} inches tall.")

print(f"He's {weight} pounds heavy.")

print("Actually that's not too heavy.")

print(f"He's got{eyes} eyes and {hair} hair.")

print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.

total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Convert inches to centimeters and pounds to kilograms

cm_conver = height * 2.54 # cm's 

kilo_conver = weight * 0.45359237 # kg's

total2 = age + cm_conver + kilo_conver

print(f"If I add {age}, {cm_conver}, and {kilo_conver} I get {total2}")

cm = 2.54

kg = 0.45359237

# Improvised round() function
total3 = age + round(height * cm) + round(weight * kg)

print(f"If I add {age}, {height} * {cm}, {weight} * {kg} I get {total3}")