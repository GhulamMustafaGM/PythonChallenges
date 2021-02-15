# Functions : Bank Deposit and Withdrawal Application

def get_info():
    """Get user information to store in a dict that represents a bank account"""
    print("\nWelcome to the Python First National Bank.")
    # Get user input
    name = input("\nHello, what is your name: ").title().strip()
    savings = int(input("How much money would you like to set up your savings account with: "))
    checking = int(input("How much money would you like to set up your checking account with: "))

    #Build a dict that represents a specific bank account
    bank_account = {
    "Name":name,
    "Savings":savings,
    "Checking":checking,
    }
    return bank_account


def make_deposit(bank_account, account, money):
    """Add money to a specific type of account"""
    bank_account[account] += money
    print("\nDeposited $" + str(money) + " into " + bank_account['Name'] + "'s " + account.lower() + " account.")


def make_withdrawal(bank_account, account, money):
    """Withdraw money from a specific type of account"""
    #Check that the balance will still be positive after the withdrawal
    if bank_account[account] - money >= 0:
        bank_account[account] -= money
        print("\nWithdrew $" + str(money) + " from " + bank_account['Name'] + "'s" + account.lower() + " account.")
    #Not enough money in the account to make the withdrawal
    else:
        print("\nSorry, by withdrawing $" + str(money) + " you will have a negative balance.")

def display_info(bank_account):
    """Display all key-value pairs in a given bank account"""
    print("\nCurrent Account Information")
    for key, value in bank_account.items():
        if key == 'Name':
            print(key + ": " + str(value))
        else:
            print(key + ": $" + str(value))

#The main code
#Create a bank account
my_account = get_info()

running = True
while running:
    #Show the current state of the bank account
    display_info(my_account)

    #Get user input for the transaction information
    account_type = input("\nWhat account would you like to access (Savings or Checking): ").title()

    choice = input("What type of transaction would you like to make (Deposit or Withdrawal): ").title()
    amount = float(input("How much money: "))

    #Make the correct function call based off previous user input
    if account_type == "Savings" or account_type == "Checking":
        if choice == "Deposit":
            make_deposit(my_account, account_type, amount)
        elif choice == "Withdrawal":
            make_withdrawal(my_account, account_type, amount)
        else:
            print("\nI'm sorry, we cannot do that for you today.")
    else:
        print("\nI'm sorry, we cannot do that for you today.")

        #Allow users to make another transaction
    choice = input("Would you like to make another transaction (y/n): ").lower()
    if choice != 'y':
        display_info(my_account)
        print("\nThank you. Have a great day!\n")
        running = False
        
# Program output

# Welcome to the Python First National Bank.

# Hello, what is your name: David Daniel
# How much money would you like to set up your savings account with: 1200
# How much money would you like to set up your checking account with: 300

# Current Account Information
# Name: David Daniel
# Savings: $1200
# Checking: $300

# What account would you like to access (Savings or Checking): savings
# What type of transaction would you like to make (Deposit or Withdrawal): deposit
# How much money: 150

# Deposited $150.0 into David Daniel's savings account.
# Would you like to make another transaction (y/n): y

# Current Account Information
# Name: David Daniel
# Savings: $1350.0
# Checking: $300

# What account would you like to access (Savings or Checking): SAVINGS
# What type of transaction would you like to make (Deposit or Withdrawal): withdrawal
# How much money: 50

# Withdrew $50.0 from David Daniel'ssavings account.
# Would you like to make another transaction (y/n): y

# Current Account Information
# Name: David Daniel
# Savings: $1300.0
# Checking: $300

# What account would you like to access (Savings or Checking): cHECKING 
# What type of transaction would you like to make (Deposit or Withdrawal): withdrawal
# How much money: 500

# Sorry, by withdrawing $500.0 you will have a negative balance.
# Would you like to make another transaction (y/n): y

# Current Account Information
# Name: David Daniel
# Savings: $1300.0
# Checking: $300

# What account would you like to access (Savings or Checking): credit
# What type of transaction would you like to make (Deposit or Withdrawal): deposit
# How much money: 40

# I'm sorry, we cannot do that for you today.
# Would you like to make another transaction (y/n): y

# Current Account Information
# Name: David Daniel
# Savings: $1300.0
# Checking: $300

# What account would you like to access (Savings or Checking): savings
# What type of transaction would you like to make (Deposit or Withdrawal): d
# How much money: 550

# I'm sorry, we cannot do that for you today.
# Would you like to make another transaction (y/n): n

# Current Account Information
# Name: David Daniel
# Savings: $1300.0
# Checking: $300

# Thank you. Have a great day!