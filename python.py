import math
# enter diameter
diameter = float(input("Enter the diameter of a circle: "))

# Calculations 
radius = diameter / 2
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Display calculations 
print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))

