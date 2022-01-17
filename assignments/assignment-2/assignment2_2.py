# Zain Raza - Assignment 2 Question 2
# Comp 2067 - Winter 2022

value = input("Enter a positive integer (digits only): ") # ask user to enter a number

if value.isdigit(): # checks if input is correct
    value = int(value)
    if value % 2 == 0: # checks if value is even
        print("You entered an even number") # confirms that even number was entered
    elif value % 7 == 0: # else if value is a multiple of 7
        print("You entered a number that is a multiple of 7") # print that it is now a multiple of 7
    else: # otherwise
        print("You entered an odd number that is NOT a multiple 7") # print it was neither
else: # otherwise
    print("You did not enter a valid input!") # print it was invalid
