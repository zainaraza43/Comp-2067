# Zain Raza - Assignment 3 Question 2
# Comp 2067 - Winter 2022

total = 0 # declaring a variable total and assigning it to 0

while total <= 100:
    num = float(input("Please enter a number: ")) # making user input for a number and casting to float

    total += num # add num to total

    print("current total =",total) # printing out the updated current total

x = total ** 2 # declaring a variable x to become the square of total

print("The square of",total,"is",round(x,1)) # printing out that x is the square of total (rounded to 1 decimal place)