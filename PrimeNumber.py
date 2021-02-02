# While Loops : Prime Number Program
import time

print("\nWelcome to the Prime Number App")

running = True

# Run the program as long as the user wants
while running:
    # Get user input
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    option = input("Enter your choice 1 or 2: ")

    # Determine if a single number is prime
    if option == '1':
        number = int(input("\nEnter a number to determine if it is prime or not:"))

        # Prime status check
        prime_status = True
        for i in range(2, number):
            if number % i == 0:
                prime_status = False
                break

        # Print summary
        if prime_status:
            print(str(number) + " is prime!")
        else:
                print(str(number) + " is not prime!")

        # Determine primes within a range of values and time the calculations
    elif option == '2':
        l_bound = int(input("\nEnter the lower bound of your range: "))
        u_bound = int(input("Enter the upper bound of your range: "))
        primes = []

        # Get the current time
        start_time = time.time()

        # Check prime status of all numbers within l_bound and u_bound
        for prime_candidate in range(l_bound, u_bound + 1):
            # 1 is not prime
            if prime_candidate > 1:
                prime_status = True
                for i in range(2, prime_candidate):
                    if prime_candidate % i == 0:
                        prime_status = False
                    break
                else:
                    prime_status = False
                    # Prime candidate is in fact prime!
                if prime_status:
                    primes.append(prime_candidate)
                    # Get the current time
                    end_time = time.time()

        # Determine the time the calculations took
        delta_time = round(end_time - start_time, 4)

        print("\nCalculations took a total of " + str(delta_time) + " seconds.")

        print("The following numbers between " + str(l_bound) + " and " + str(u_bound) + " are prime: ")
        input("Press enter to continue.")

        for prime in primes:
            print(prime)
        # Not a valid choice entered by the user
        else:
            print("\nThat is not a valid option.")

        # Quit the program if the user does not enter in y
        choice = input("Would you like to run the program again (y/n): ").lower()
        if choice != 'y':
            running = False
            print("\nThank you for using the program. Have a nice day.\n")
            

# Program output 

# Welcome to the Prime Number App

# Enter 1 to determine if a specific number is prime.       
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 1

# Enter a number to determine if it is prime or not:55
# 55 is not prime!

# Enter 1 to determine if a specific number is prime.
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 1

# Enter a number to determine if it is prime or not:11
# 11 is prime!

# Enter 1 to determine if a specific number is prime.
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 2

# Enter the lower bound of your range: 1
# Enter the upper bound of your range: 11

# Calculations took a total of 0.0 seconds.
# The following numbers between 1 and 11 are prime:
# Press enter to continue.
# 3
# 5
# 7
# 9
# 11

# That is not a valid option.
# Would you like to run the program again (y/n): y

# Enter 1 to determine if a specific number is prime.
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 1

# Enter a number to determine if it is prime or not:12
# 12 is not prime!

# Enter 1 to determine if a specific number is prime.
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 1

# Enter a number to determine if it is prime or not:21
# 21 is not prime!

# Enter 1 to determine if a specific number is prime.
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 1

# Enter a number to determine if it is prime or not:11
# 11 is prime!

# Enter 1 to determine if a specific number is prime.       
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 1

# Enter a number to determine if it is prime or not:11
# 11 is prime!

# Enter 1 to determine if a specific number is prime.       
# Enter 2 to determine all prime numbers within a set range.
# Enter your choice 1 or 2: 2

# Enter the lower bound of your range: 1
# Enter the upper bound of your range: 100

# Calculations took a total of 0.001 seconds.        
# The following numbers between 1 and 100 are prime: 
# Press enter to continue.
# 3 
# 5 
# 7 
# 9 
# 11
# 13
# 15
# 17
# 19
# 21
# 23
# 25
# 27
# 29
# 31
# 33
# 35
# 37
# 39
# 41
# 43
# 45
# 47
# 49
# 51
# 53
# 55
# 57
# 59
# 61
# 63
# 65
# 67
# 69
# 71
# 73
# 75
# 77
# 79
# 81
# 83
# 85
# 87
# 89
# 91
# 93
# 95
# 97
# 99

# That is not a valid option.
# Would you like to run the program again (y/n):