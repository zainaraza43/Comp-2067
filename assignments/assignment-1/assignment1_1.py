# Zain Raza - Assignment 1 Question 1
# Comp 2067 - Winter 2022

books = int(input("Please enter the number of books: ")) # user input for number of books casted to an int

boxes = books / 15 # algorithm for number of boxes

print("You will need",boxes,"box(es) for your books.") # printing float number of boxes
print("You will need",round(boxes),"FULL box(es) for your books.") # printing full number of boxes