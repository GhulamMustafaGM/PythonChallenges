
import math

print("Welcome to the Right Triangle Solver App")

# Get user input
side_a = float(input("\nWhat is the first leg of the triangle: "))
side_b = float(input("What is the second leg of the triangle: "))

# Calculations
side_c = math.sqrt(side_a**2 + side_b**2)
side_c = round(side_c, 3)

area = 0.5*side_a*side_b
area = round(area, 3)

# Summary
print("\nFor a triangle with legs of " + str(side_a) + " and " + str(side_b) + " hypotenuse is " + str(side_c) + ".")
print("For a triangle with legs of " + str(side_a) + " and " + str(side_b) + " the area is " + str(area) + ".")


# output

# Welcome to the Right Triangle Solver App

# What is the first leg of the triangle: 30
# What is the second leg of the triangle: 50.5

# For a triangle with legs of 30.0 and 50.5 hypotenuse is 58.739.
# For a triangle with legs of 30.0 and 50.5 the area is 757.5.