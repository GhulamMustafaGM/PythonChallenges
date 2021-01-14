# Lists Challenge - Favorite Teachers Program

print("\nWelcome to the Favorite Teachers Program")
fav_teachers = []

# Get user input
fav_teachers.append(input("\nWho is your first favorite teacher: ").title())
fav_teachers.append(input("Who is your second favorite teacher: ").title())
fav_teachers.append(input("Who is your third favorite teacher: ").title())
fav_teachers.append(input("Who is your fourth favorite teacher: ").title())

# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".") 
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Insert a new favorite teacher
fav_teachers.insert(0, input("\nOops, " + fav_teachers[0] + " is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title())

# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Remove a specific teacher
fav_teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title())

# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers))) 
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse=True)))
print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Output

# Who is your first favorite teacher: Max
# Who is your second favorite teacher: David
# Who is your third favorite teacher: John
# Who is your fourth favorite teacher: Thomas

# Your favorite teachers ranked are: ['Max', 'David', 'John', 'Thomas']
# Your favorite teachers alphabetically are: ['David', 'John', 'Max', 'Thomas']
# Your favorite teachers in reverse alphabetical order are: ['Thomas', 'Max', 'John', 'David']

# Your top two teachers are: Max and David.
# Your next two favorite teachers are: John and Thomas.
# Your last favorite teacher is: Thomas.
# You have a total of 4 favorite teachers.

# Oops, Max is no longer your first favorite teacher. Who is your new FAVORITE teacher: David

# Your favorite teachers ranked are: ['David', 'Max', 'David', 'John', 'Thomas']
# Your favorite teachers alphabetically are: ['David', 'David', 'John', 'Max', 'Thomas']
# Your favorite teachers in reverse alphabetical order are: ['Thomas', 'Max', 'John', 'David', 'David']

# Your top two teachers are: David and Max.
# Your next two favorite teachers are: David and John.
# Your last favorite teacher is: Thomas.
# You have a total of 5 favorite teachers.

# You've decided you no longer like a teacher. Which teacher would you like to remove from your list: John

# Your favorite teachers ranked are: ['David', 'Max', 'David', 'Thomas']
# Your favorite teachers alphabetically are: ['David', 'David', 'Max', 'Thomas']
# Your favorite teachers in reverse alphabetical order are: ['Thomas', 'Max', 'David', 'David']

# Your top two teachers are: David and Max.
# Your next two favorite teachers are: David and Thomas.
# Your last favorite teacher is: Thomas.
# You have a total of 4 favorite teachers.
