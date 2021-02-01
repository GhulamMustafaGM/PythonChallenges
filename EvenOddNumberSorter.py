# While Loops : Even Odd Number Sorter App

print("\nWelcome to the Even Odd Number Sorter App")

running = True

# Run the program as longs as the user wants
while running:
    # Get user input
    num_string = input("\nEnter in a string of numbers separated by a comma (,) :")
    num_string = num_string.replace(' ', '')
    num_list = num_string.split(",")

    # Initialize lists to hold even/odd values
    evens = []
    odds = []

    # Calculate whether the number is even or odd
    print("\n---- Result Summary ----")
    for number in num_list:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            print("\t" + str(number) + " is even!")
        else:
            odds.append(number)
            print("\t" + str(number) + " is odd!")

        # Sort the lists evens and odds
        evens.sort()
        odds.sort()

    # Show the even numbers
    print("\nThe following " + str(len(evens)) + " numbers are even: ")
    for even in evens:
        print("\t" + str(even))

    # Show the odd numbers
    print("\nThe following " + str(len(odds)) + " numbers are odd: ")
    for odd in odds:
        print("\t" + str(odd))

    # Quit the program if the user does not enter in 'y'
    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using the program. Goodbye.\n") 
        
# Program output 

# Welcome to the Even Odd Number Sorter App

# Enter in a string of numbers separated by a comma (,) :1,2,3,5,7,9,8,22

# ---- Result Summary ----
#         1 is odd!       
#         2 is even!      
#         3 is odd!       
#         5 is odd!       
#         7 is odd!
#         9 is odd!
#         8 is even!
#         22 is even!

# The following 3 numbers are even:
#         2
#         8
#         22

# The following 5 numbers are odd:
#         1
#         3
#         5
#         7
#         9

# Would you like to run the program again (y/n): n
# Thank you for using the program. Goodbye.