# Functions Challenge 32: The Python Calculator App

def add(a, b):
    """Add two numbers and return the sum"""
    summation = round(a+b, 4)
    print("The sum of " + str(a) + " and " + str(b) + " is " + str(summation) + ".")
    return str(a) + " + " + str(b) + " = " + str(summation)

def subtract(a, b):
    """Subtract two numbers and return the difference"""
    difference = round(a-b, 4)
    print("The difference of " + str(a) + " and " + str(b) + " is " + str(difference) + ".")
    return str(a) + " - " + str(b) + " = " + str(difference)


def multiply(a, b):
    """Multiply two numbers and return the product"""
    product = round(a*b, 4)
    print("The product of " + str(a) + " and " + str(b) + " is " + str(product) + ".")
    return str(a) + " * " + str(b) + " = " + str(product)


def divide(a, b):
    """Divide two numbers and return the quotient"""
    # Perform the division if the denominator is not zero
    if b != 0:
        quotient = round(a/b, 4)
        print("The quotient of " + str(a) + " and " + str(b) + " is " + str(quotient) + ".")
        return str(a) + " / " + str(b) + " = " + str(quotient)
        # Denominator is zero, result in error
    else:
        print("You cannot divide by zero.")
        return "DIV ERROR"

def exponent(a, b):
    """Take a number to a power and return the result"""
    power = round(a**b, 4)
    print("The result of " + str(a) + " raised to the " + str(b) + " power is " + str(power) + ".")
    return str(a) + " ** " + str(b) + " = " + str(power)

# The main code
print("\nWelcome to the Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")

history = []
running = True

while running:
    # Get user input
    num1 = float(input("\nEnter a number: "))
    num2 = float(input("Enter a number: "))
    operator = input("Enter an operation(addition, subtraction, multiplication, division, or exponentiation): ").lower()\
    # Call the appropriate function based on the value of operator if operator == 'addition' or operator == 'a':     result=add(num1, num2) elif operator == 'subtraction' or operator == 's': result=subtract(num1, num2) elif operator == 'multiplication' or operator == 'm': result=multiply(num1, num2) elif operator == 'division' or operator == 'd': result=divide(num1, num2) elif operator == 'exponentiation' or operator == 'e': result=exponent(num1, num2)  else: print("That is not a valid operation. Try again.")
    if operator == 'addition' or operator == 'a':
        result = add(num1, num2)
    elif operator == 'subtraction' or operator == 's':
        result = subtract(num1, num2)
    elif operator == 'multiplication' or operator == 'm':
        result = multiply(num1, num2)
    elif operator == 'division' or operator == 'd':
        result = divide(num1, num2)
    elif operator == 'exponentiation' or operator == 'e':
        result = exponent(num1, num2)
    else:
        print("That is not a valid operation. Try again.")
        result = "OPP ERROR"

    #Append the mathematical result to the history
    history.append(result)

    #Allow user to quit
    choice = input("Would you like to run the program again (y/n): ").lower()
    if choice != 'y':
        print("\nCalculation Summary: ")
        for calc in history:
            print(calc)
        print("\nThank you for using the Python Calculator App. Goodbye.")
        running = False


# Program output 

# Welcome to the Python Calculator App
# Enter two numbers and an operation and the desired operation will be performed.

# Enter a number: 5
# Enter a number: 8
# Enter an operation(addition, subtraction, multiplication, division, or exponentiation): addition
# The sum of 5.0 and 8.0 is 13.0.
# Would you like to run the program again (y/n): y

# Enter a number: 10
# Enter a number: 22
# Enter an operation(addition, subtraction, multiplication, division, or exponentiation): s
# The difference of 10.0 and 22.0 is -12.0.      
# Would you like to run the program again (y/n): y

# Enter a number: 3.22
# Enter a number: .6
# Enter an operation(addition, subtraction, multiplication, division, or exponentiation): multiplication
# The product of 3.22 and 0.6 is 1.932.
# Would you like to run the program again (y/n): y

# Enter a number: 4
# Enter a number: 0
# Enter an operation(addition, subtraction, multiplication, division, or exponentiation): D
# You cannot divide by zero.
# Would you like to run the program again (y/n): y

# Enter a number: 4
# Enter a number: 2.5
# Enter an operation(addition, subtraction, multiplication, division, or exponentiation): square root
# That is not a valid operation. Try again.
# Would you like to run the program again (y/n): y

# Enter a number: 4
# Enter a number: 3
# Enter an operation(addition, subtraction, multiplication, division, or exponentiation): exponentiation
# The result of 4.0 raised to the 3.0 power is 64.0.
# Would you like to run the program again (y/n): n

# Calculation Summary:
# 5.0 + 8.0 = 13.0
# 10.0 - 22.0 = -12.0
# 3.22 * 0.6 = 1.932
# DIV ERROR
# OPP ERROR
# 4.0 ** 3.0 = 64.0

# Thank you for using the Python Calculator App. Goodbye.