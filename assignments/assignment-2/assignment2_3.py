# Zain Raza - Assignment 2 Question 3
# Comp 2067 - Winter 2022

L1 = [5, -34, 0, 98, -11, 244, 193, 28, -10, -20, 45, 67] # given list

print("L1 =",L1) # print list

x = int(input("Enter an integer in the range 0 to 11: ")) # user input for a range, cast to int

if 0 <= x <= len(L1) - 1: # check if x in range of list
    print("the x_th element of L1 is:", L1[x]) # print L1(x)
    if x in L1: # if x occurs in L1
        print(x,"occurs in L1 at position:",L1.index(x)) # print position number
    else: # otherwise
        print(x,"does not occur in L1") # print x doesn't occur
    if x % 2 == 0 and x > 0: # check for even number and greater than 0
        print("The first",x,"elements of L1:",L1[0:x]) # print first x elements in list
    elif x % 2 == 1 and x > 0: # check for odd number and greater than 0
        print("The last",x,"elements of L1:",L1[x+1:len(L1)-1]) # print last 5 elements
    else: # x = 0
        print([]) # print empty list
else: # not in range
    print("You did not enter a valid input!") # error message