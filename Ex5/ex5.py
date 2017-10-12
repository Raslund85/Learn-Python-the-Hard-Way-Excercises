name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually it's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + weight + height
print(f"If I add {age}, {height}, and {weight} I get {total}")


#Study Drills:

print("Conversion from lbs to kg")
print("=" * 20)			#Writes = 20 times on same line
customLBS = 200
kg = round(customLBS / 2.2046226218488, 2)
print(f"{customLBS} is {kg} kg")