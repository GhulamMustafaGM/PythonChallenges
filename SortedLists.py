# Sorted lists numbers

num_strings = ['25', '100', '61', '49']
num_ints = [10, 100, 59, 49]
num_floats = [2.4, 6.0, 1.245, 0.242857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Summary of each list
print("\t\tSummary Table")

print("\nThe variable num_strings is a " + str(type(num_strings)) + ".")
print("It contains the elements: " + str(num_strings))
print("The element " + num_strings[0] + " is a " + str(type(num_strings[0])) + ".")

print("\nThe variable num_ints is a " + str(type(num_ints)) + ".")
print("It contains the elements: " + str(num_ints))
print("The element " + str(num_ints[0]) + " is a " + str(type(num_ints[0])) + ".")

print("\nThe variable num_floats is a " + str(type(num_floats)) + ".")
print("It contains the elements: " + str(num_floats))
print("The element " + str(num_floats[0]) + " is a " + str(type(num_floats[0])) + ".")

print("\nThe variable num_lists is a " + str(type(num_lists)) + ".")
print("It contains the elements: " + str(num_lists)) 
print("The element " + str(num_lists[0]) + " is a " + str(type(num_lists[0])) + ".")

# Sorting the lists
num_strings.sort()
num_ints.sort()

print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " + str(num_strings))
print("Sorted num_ints: " + str(num_ints))
print("\nStrings are sorted alphabetically while integers are sorted numerically!!!")

# output

# The variable num_strings is a <class 'list'>.      
# It contains the elements: ['25', '100', '61', '49']
# The element 25 is a <class 'str'>.

# The variable num_ints is a <class 'list'>.
# It contains the elements: [10, 100, 59, 49]        
# The element 10 is a <class 'int'>.

# The variable num_floats is a <class 'list'>.
# It contains the elements: [2.4, 6.0, 1.245, 0.242857]
# The element 2.4 is a <class 'float'>.

# The variable num_lists is a <class 'list'>.
# It contains the elements: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# The element [1, 2, 3] is a <class 'list'>.

# Now sorting num_strings and num_ints...
# Sorted num_strings: ['100', '25', '49', '61']
# Sorted num_ints: [10, 49, 59, 100]

# Strings are sorted alphabetically while integers are sorted numerically!!!