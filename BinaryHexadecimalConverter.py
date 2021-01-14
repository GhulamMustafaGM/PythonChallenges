# Binary Hexadecimal Converter App
print("\nWelcome to the Binary/Hexadecimal Converter App")

# Get user input and generate lists.
max_value = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value+1))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
    print("Generating lists...Complete!")

    # Get slicing index from user.
    print("\nUsing slices, we will now show a portion of each list.")
    lower_range = int(
        input("What decimal number would you like to start at: "))
    upper_range = int(input("What decimal number would you like to stop at: "))

    # Slice through each list individually
    print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")
    for num in decimal[lower_range-1:upper_range]:
        print(num)

    print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) + ":")
    for num in binary[lower_range-1:upper_range]: 
        print(num)

    print("\nHexadecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")
    for num in hexadecimal[lower_range-1:upper_range]:
        print(num)

    # Output the whole list to the screen
    input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
    print("Decimal----Binary----Hexadecimal")
    print("----------------------------------------------")
    for d, b, h in zip(decimal, binary, hexadecimal):
        print(str(d) + "----" + str(b) + "----" + str(h))

# Output

# Welcome to the Binary/Hexadecimal Converter App

# Compute binary and hexadecimal values up to the following decimal number: 14
# Generating lists...Complete!

# Using slices, we will now show a portion of each list.
# What decimal number would you like to start at: 6
# What decimal number would you like to stop at: 9

# Decimal values from 6 to 9:
# 6
# 7
# 8
# 9

# Binary values from 6 to 9:

# Hexadecimal values from 6 to 9:

# Press Enter to see all values from 1 to 14.
# Decimal----Binary----Hexadecimal
# ----------------------------------------------
# 1----0b1----0x1
# Generating lists...Complete!