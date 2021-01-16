# For Loops: Factorial Calculator App
import math

print("\n Welcome to the Factorial Calculator App")

# Get user input
number = int(input("\nWhat number would you like to compute the factorial of: "))

# Display the mathematical relationship of a factorial
print(str(number) + "! = ", end="")
for i in range(1, number):
    print(str(i), end="*")
    print(str(number))

#Using the math library
fact = math.factorial(number)
print("\nHere is the result from the math library: ")
print("The factorial of " + str(number) + " is " + str(fact) + "!")

# Using my own algorithm
fact = 1
for i in range(1, number+1):
    fact = fact*i
    print("\nHere is the result from my own algorithm: ")
    print("The factorial of " + str(number) + " is " + str(fact) + "!")

# Summary
print("\nIt is shown twice that" + str(number) + "! = " + str(fact) + " (with excitement!) \n")

# Output

# Welcome to the Factorial Calculator App

# What number would you like to compute the factorial of: 12
# 12! = 1*12
# 2*12      
# 3*12      
# 4*12      
# 5*12      
# 6*12      
# 7*12
# 8*12
# 9*12
# 10*12
# 11*12

# Here is the result from the math library:
# The factorial of 12 is 479001600!

# Here is the result from my own algorithm:
# The factorial of 12 is 1!

# Here is the result from my own algorithm:
# The factorial of 12 is 2!

# Here is the result from my own algorithm:
# The factorial of 12 is 6!

# Here is the result from my own algorithm:
# The factorial of 12 is 24!

# Here is the result from my own algorithm:
# The factorial of 12 is 120!

# Here is the result from my own algorithm:
# The factorial of 12 is 720!

# Here is the result from my own algorithm:
# The factorial of 12 is 5040!

# Here is the result from my own algorithm:
# The factorial of 12 is 40320!

# Here is the result from my own algorithm:
# The factorial of 12 is 362880!

# Here is the result from my own algorithm:
# The factorial of 12 is 3628800!

# Here is the result from my own algorithm:
# The factorial of 12 is 39916800!

# Here is the result from my own algorithm:
# The factorial of 12 is 479001600!

# It is shown twice that12! = 479001600 (with excitement!)

