# Multiplication and Exponent Table App

print("Welcome to the Multiplication/Exponent Table Program")

# Gather user input
name = input("\nHello, what is your name: ").title().strip()
num = float(input("What number would you like to work with: "))
message = name + ", Math is cool!"

# Multiplication table
print("\nMultiplication Table For " + str(num))
print("\n\t 1.0 * " + str(num) + " = " + str(round(1*num, 4)))
print("\t 2.0 * " + str(num) + " = " + str(round(2*num, 4)))
print("\t 3.0 * " + str(num) + " = " + str(round(3*num, 4)))
print("\t 4.0 * " + str(num) + " = " + str(round(4*num, 4)))
print("\t 5.0 * " + str(num) + " = " + str(round(5*num, 4)))
print("\t 6.0 * " + str(num) + " = " + str(round(6*num, 4)))
print("\t 7.0 * " + str(num) + " = " + str(round(7*num, 4)))
print("\t 8.0 * " + str(num) + " = " + str(round(8*num, 4)))
print("\t 9.0 * " + str(num) + " = " + str(round(9*num, 4)))

# Exponent table
print("\nExponent Table For " + str(num))
print("\n\t" + str(num) + " ** 1 = " + str(round(num**1, 4)))
print("\t" + str(num) + " ** 2 = " + str(round(num**2, 4)))
print("\t" + str(num) + " ** 3 = " + str(round(num**3, 4)))
print("\t" + str(num) + " ** 4 = " + str(round(num**4, 4)))
print("\t" + str(num) + " ** 5 = " + str(round(num**5, 4)))
print("\t" + str(num) + " ** 6 = " + str(round(num**6, 4)))
print("\t" + str(num) + " ** 7 = " + str(round(num**7, 4)))
print("\t" + str(num) + " ** 8 = " + str(round(num**8, 4)))
print("\t" + str(num) + " ** 9 = " + str(round(num**9, 4)))

# Math is cool!
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())

# output

# Welcome to the Multiplication/Exponent Table Program

# Hello, what is your name: David
# What number would you like to work with: 2

# Multiplication Table For 2.0

#          1.0 * 2.0 = 2.0
#          2.0 * 2.0 = 4.0
#          3.0 * 2.0 = 6.0
#          4.0 * 2.0 = 8.0
#          5.0 * 2.0 = 10.0
#          6.0 * 2.0 = 12.0
#          7.0 * 2.0 = 14.0
#          8.0 * 2.0 = 16.0
#          9.0 * 2.0 = 18.0

# Exponent Table For 2.0

#         2.0 ** 1 = 2.0
#         2.0 ** 2 = 4.0
#         2.0 ** 3 = 8.0
#         2.0 ** 4 = 16.0
#         2.0 ** 5 = 32.0
#         2.0 ** 6 = 64.0
#         2.0 ** 7 = 128.0
#         2.0 ** 8 = 256.0
#         2.0 ** 9 = 512.0

# David, Math is cool!
#         david, math is cool!
#                 David, Math Is Cool!
#                         DAVID, MATH IS COOL!