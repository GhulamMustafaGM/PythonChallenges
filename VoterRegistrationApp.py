# Conditionals: Voter Registration App

print("\nWelcome to the Voter Registration App")

# Get user input
name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

# Define our list of political parties
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

# If the user is 18 or older, they can register to vote
if age > 17:
    print("\nCongratulations " + name + "! You are old enough to register to vote.")
    print("\nHere is a list of political parties to join.")

    # Display our political parties
    for party in parties:
        print("\t- " + party)

    # Get user input for the party they wish to join
    chosen_party = input("\nWhat party would you like to join: ").title().strip()

    # Print a message specific to the party chosen
    if chosen_party in parties:
        print("\nCongratulations " + name + "! You have joined the " + chosen_party + " party!")
        if chosen_party == "Republican" or chosen_party == "Democratic":
            print("That is a major party!\n")
        elif chosen_party == "Independent":
            print("You are an independent person!\n")
        else:
            print("That is not a major party.\n")
    else:
        print("That is not a given party.\n")

    # Else the user is younger than 18 years old
else:
    print("\nYou are not old enough to register to vote.\n")

# Program output

# Welcome to the Voter Registration App

# Please enter your name: David
# Please enter your age: 29

# Congratulations David! You are old enough to register to vote.

# Here is a list of political parties to join.
#         - Republican
#         - Democratic
#         - Independent
#         - Libertarian
#         - Green

# What party would you like to join: Democratic

# Congratulations David! You have joined the Democratic party!
# That is a major party!

# Program output 2

# Welcome to the Voter Registration App

# Please enter your name: James
# Please enter your age: 15

# You are not old enough to register to vote.