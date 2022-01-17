# Zain Raza - Assignment 2 Question 1
# Comp 2067 - Winter 2022

name = input("Enter your first name:") # user input for their name

if name[0].lower() == "a" or name[0].lower() == "e" or name[0].lower() == "i" or name[0].lower() == "o" or name[0].lower() == "u": # Checks for vowel letters and forces to lower case so that capitals are recognized as well
    print("Your name starts with a vowel.") # confirm that they start with a vowel
else:
    print("Your name starts with a consonant") # confirm that they start with a consonant

print("The first letter of your name is:",name[0].upper()) # upper case version of the first letter of name