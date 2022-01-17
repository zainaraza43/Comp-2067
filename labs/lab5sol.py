# Zain Raza - Lab 5
# Comp 2067 - Winter 2022

x = int(input("Enter an integer between 0 and 8: ")) # user input for an integer, casting to int

counter = 0 # counter for number of times loop is run

while x < 50: # while x is less than 50
    counter += 1
    print(x) # print x
    if x % 9 == 0: # if x is a multiple of 9
        print("found multiple of 9") # print that it is
        break # break from loop
    x += 10 # add 10 to x

print("The final value of x is", x) # print final value of x
print("The loop was entered",counter,"times.") # print number of times loop was used