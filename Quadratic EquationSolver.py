# For Loops: Quadratic Equation Solver App
import cmath

# Print Welcome Information
print("\nWelcome to the Quadratic Equation Solver App")
print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

    # Get user input
eq_number = int(input("\nHow many equations would you like to solve today: "))

# Loop through and solve each equation
for i in range(eq_number):
    print("\nSolving equation #" + str(i+1))
    print("--------------------------------------------------")
    a = float(input("\nPlease enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))

# Solving the quadratic formula
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)

    print("\nThe solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are: ")
    print("\n\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))

    print("\nThank you for using the Quadratic Equation Solver App. Goodbye.\n")
    
#    Output 
    
# Welcome to the Quadratic Equation Solver App

# A quadratic equation is of the form ax^2 + bx + c = 0
# Your solutions can be real or complex numbers.
# A complex number has two parts: a + bj
# Where a is the real portion and bj is the imaginary portion.

# How many equations would you like to solve today: 2

# Solving equation #1
# --------------------------------------------------

# Please enter your value of a (coefficient of x^2): 1
# Please enter your value of b (coefficient of x): 8
# Please enter your value of c (coefficient): 9

# The solutions to 1.0x^2 + 8.0x + 9.0 = 0 are:

#         x1 = (-1.3542486889354093+0j)
#         x2 = (-6.645751311064591+0j)

# Thank you for using the Quadratic Equation Solver App. Goodbye.

# Solving equation #2
# --------------------------------------------------

# Please enter your value of a (coefficient of x^2): 2
# Please enter your value of b (coefficient of x): 4
# Please enter your value of c (coefficient): 10

# The solutions to 2.0x^2 + 4.0x + 10.0 = 0 are:

#         x1 = (-1+2j)
#         x2 = (-1-2j)

# Thank you for using the Quadratic Equation Solver App. Goodbye.