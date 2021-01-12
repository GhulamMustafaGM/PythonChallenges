# Grade Sorter App

print("Welcome to the Grade Sorter App")

# Initialize list and get user input
grades = []
grade = int(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your second grade (0-100): "))
grades.append(grade)
grade = int(input("What is your third grade (0-100): "))
grades.append(grade)
grade = int(input("What is your fourth grade (0-100): "))
grades.append(grade)

print("\nYour grades are: " + str(grades))

# Sort the list from highest to lowest
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades))

# Removing the lowest two grades.
print("\nThe lowest two grades will now be dropped.")
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))

# Recap remaining grades
print("\nYour remaining grades are: " + str(grades))
print("Nice work! Your highest grade is " + str(grades[0]) + ".")

# output 

# Welcome to the Grade Sorter App

# What is your first grade (0-100): 98
# What is your second grade (0-100): 85
# What is your third grade (0-100): 76
# What is your fourth grade (0-100): 73

# Your grades are: [98, 85, 76, 73]

# Your grades from highest to lowest are: [98, 85, 76, 73]

# The lowest two grades will now be dropped.
# Removed grade: 73
# Removed grade: 76

# Your remaining grades are: [98, 85]
# Nice work! Your highest grade is 98.