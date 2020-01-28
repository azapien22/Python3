my_name = "Zed A. Shaw"
my_age = 34
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = "Brown"
my_teeth = "white"
my_hair = "brown"

inches = 74
cm = inches * 2.54
print(f"Inches({inches}) => CM({round(cm,3)})")

pounds = 180
kg = pounds * 0.453592
print(f"({pounds})pounds => ({round(kg,4)})kg")
print(f"Zed is {kg} kilograms") 

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall. Another way to express this is to say he is {cm} centimeters tall.")
print(f"He's {my_weight} pounds heavy. Another way to express this is to say he is {kg} kilograms")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
