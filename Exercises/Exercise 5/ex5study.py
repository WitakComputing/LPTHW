name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = 74 * 2.54
weight = 180 # lbs
weight_kg = 180 / round(2.20462262)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get {total}.")
