# Dictionaries: Frequency Analysis App
from collections import Counter

print("\nWelcome to the Frequency Analysis App")

# List of elements to remove from all text for analysis
non_letters = ['1','2','3','4','5','6','7','8','9','0',' ',
'.','?','!',',','"',"'",':',';','(',')','%','$','&','#','\n','\t']

# Information for the first key key_phrase_1
key_phrase_1 = input("Enter a word or phrase to count the occurrence of each letter: ").lower().strip()

# Removing all non letters from key_phrase_1
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_1)

# Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage) + "%")

# Make a list of letters from highest occurrence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

# Print the list
print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_1_ordered_letters:
    print(letter, end='')

# Information for the second key key_phrase_2
key_phrase_2 = input("\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()

# Removing all non letters from key_phrase_2
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurrences = len(key_phrase_2)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_2)

# Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage) + "%")

# Make a list of letters from highest occurrence to lowest
ordered_letter_count = letter_count.most_common()

key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])

# Print the list
print("\nLetters ordered from highest occurrence to lowest: \n")
for letter in key_phrase_2_ordered_letters:
    print(letter, end='')


# Program output

# Welcome to the Frequency Analysis App
# Enter a word or phrase to count the occurrence of each letter: Hi, What is up?

# Here is the frequency analysis from key phrase 1: 

#         Letter          Occurrence      Percentage
#         a               1               10.0%
#         h               2               20.0%
#         i               2               20.0%
#         p               1               10.0%
#         s               1               10.0%
#         t               1               10.0%
#         u               1               10.0%
#         w               1               10.0%

# Letters ordered from highest occurrence to lowest:
# hiwatsup

# Enter a word or phrase to count the occurrence of each letter: Thanks, I am pretty good.

# Here is the frequency analysis from key phrase 2: 

#         Letter          Occurrence      Percentage
#         a               2               10.53%    
#         d               1               5.26%     
#         e               1               5.26%     
#         g               1               5.26%     
#         h               1               5.26%     
#         i               1               5.26%     
#         k               1               5.26%     
#         m               1               5.26%     
#         n               1               5.26%     
#         o               2               10.53%    
#         p               1               5.26%     
#         r               1               5.26%     
#         s               1               5.26%     
#         t               3               15.79%    
#         y               1               5.26%

# Letters ordered from highest occurrence to lowest:

# taohnksimpreygd