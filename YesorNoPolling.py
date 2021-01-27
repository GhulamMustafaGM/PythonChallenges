# Dictionaries: Yes or No Polling App

print("\nWelcome to the Yes or No Issue Polling ")

#Get user input
issue = input("\nWhat is the yes or no issue you will be voting on today: ")
vote_number = int(input("what is the number of voters you will allow on the issue: "))
password = input("Enter a password for the polling results: ")

# Initialize our variables
yes = 0
no = 0
results = {}

#Simulate voting
for i in range(vote_number):
    name = input("\nEnter your full name: ").title().strip()
    if name in results.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print("Here is our issue: " + issue)
        choice = input("What do you think...yes or no: ").lower().strip()
        if choice == 'yes' or choice == 'y':
            choice = 'yes'
            yes += 1
        elif choice == 'no' or choice == 'n':
            choice = 'no'
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")
    
#Add vote to the dictionary results
results[name] = choice
print("Thank you " + name + "! Your vote of " + results[name] + " has been recorded.")

# Show who actually voted
total_votes = len(results.keys())
print("\nThe following " + str(total_votes) + " people voted: ")
for key in results.keys():
    print(key)

#Summarize the voting results
print("\nOn the following issue: " + issue)
if yes > no:
        print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no > yes:
    print("No wins! " + str(no) + " votes to " + str(yes) + ".")
else:
    print("It was a tie! " + str(no) + " votes to " + str(yes) + ".")

#Allow the admin to see the actual votes
guess = input("\nTo see the voting results enter the admin password: ")
if guess == password:
    for key, value in results.items():
        print("Voter: " + key + "\t\t\tVote: " + value)
    else:
        print("Sorry, that is not the correct password. Goodbye...")

print("\nThank you for using the Yes or No Issue Polling App.\n")

# Program output 

# Welcome to the Yes or No Issue Polling

# What is the yes or no issue you will be voting on today: Should soda be banned for young children?
# what is the number of voters you will allow on the issue: 4
# Enter a password for the polling results: 1234

# Enter your full name: john doe
# Here is our issue: Should soda be banned for young children?
# What do you think...yes or no: yes

# Enter your full name: david
# Here is our issue: Should soda be banned for young children?
# What do you think...yes or no: YES

# Enter your full name: lena jane
# Here is our issue: Should soda be banned for young children?
# What do you think...yes or no: N

# Enter your full name: Tony blayer
# Here is our issue: Should soda be banned for young children?
# What do you think...yes or no: yes
# Thank you Tony Blayer! Your vote of yes has been recorded.

# The following 1 people voted:
# Tony Blayer

# On the following issue: Should soda be banned for young children?
# Yes wins! 3 votes to 1.

# To see the voting results enter the admin password: admin1234

# Thank you for using the Yes or No Issue Polling App.