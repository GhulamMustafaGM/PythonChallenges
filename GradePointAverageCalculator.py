# For Loops: Grade Point Average Calculator App

print("\nWelcome to the Grade Point Average Calculator App")

# Get user input
name = input("What is your name: ").title().strip()
grade_num = int(input("How many grades would you like to enter: "))

# Get the user's grades
grades = []
for i in range(grade_num):
    grades.append(int(input("Enter grade: ")))

# Sort the grades and print them to the screen
grades.sort(reverse=True)
print("\nGrades Highest to Lowest:")
for grade in grades:
    print("\t" + str(grade))

# Calculate the average
average = sum(grades)/len(grades)
average = round(average, 2)

# Print a grade summary
print("\n" + name + "'s Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades)))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage: " + str(average))

# Get the user's desired average and calculate what they need to get on the next assignment
desired_avg = float(input("\nWhat is your desired average: "))
grade_req = desired_avg*(len(grades)+1) - sum(grades)
grade_req = round(grade_req, 2)

# Print a summary
print("\nGood luck " + name + "!")
print("You will need to get a " + str(grade_req) + " on your next assignment to earn a " + str(desired_avg) + " average.")

# Make a copy of the original grades and swap out one of the grades
new_grades = grades[:]
print("\nLets see what you average could have been if you did better/worse on an assignment.")
grade_change = int(input("What grade would you like to change: "))
new_grades.remove(grade_change)
new_grade = int(input("What grade would you like to change " + str(grade_change) + " to: "))
new_grades.append(new_grade)

# Sort the new grades and print them to the screen
new_grades.sort(reverse=True)
print("\nNew Grades Highest to Lowest:")
for grade in new_grades:
    print("\t" + str(grade))

# Calculate the new average
new_average = sum(new_grades)/len(new_grades)
new_average = round(new_average, 2)

# Print a new grade summary
print("\n" + name + "'s New Grade Summary:")
print("\tTotal Number of Grades: " + str(len(new_grades)))

print("\tHighest Grade: " + str(max(new_grades)))
print("\tLowest Grade: " + str(min(new_grades)))
print("\tAverage: " + str(new_average))

# Print a summary on how the average changed
print("\nYour new average would be a " + str(new_average) + " compared to your real average of " + str(average) + "!")
average_change = new_average - average
average_change = round(average_change, 2)
print("That is a change of " + str(average_change) + " points!")

# Too bad the original grades are still intact!
print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go ask for extra credit!\n")

# Program output

# Welcome to the Grade Point Average Calculator App
# What is your name: Johone Doe
# How many grades would you like to enter: 7
# Enter grade: 89
# Enter grade: 90
# Enter grade: 89
# Enter grade: 69
# Enter grade: 77
# Enter grade: 77
# Enter grade: 89

# Grades Highest to Lowest:
#         90
#         89
#         89
#         89
#         77
#         77
#         69

# Johone Doe's Grade Summary:
#         Total Number of Grades: 7
#         Highest Grade: 90
#         Lowest Grade: 69
#         Average: 82.86

# What is your desired average: 90

# Good luck Johone Doe!
# You will need to get a 140.0 on your next assignment to earn a 90.0 average.

# Lets see what you average could have been if you did better/worse on an assignment.
# What grade would you like to change: 69
# What grade would you like to change 69 to: 75

# New Grades Highest to Lowest:
#         90
#         89
#         89
#         89
#         77
#         77
#         75

# Johone Doe's New Grade Summary:
#         Total Number of Grades: 7
#         Highest Grade: 90
#         Lowest Grade: 75
#         Average: 83.71

# Your new average would be a 83.71 compared to your real average of 82.86!
# That is a change of 0.85 points!

# Too bad your original grades are still the same!
# [90, 89, 89, 89, 77, 77, 69]
# You should go ask for extra credit!