# Zain Raza - Lab 4
# Comp 2067 - Winter 2022

myint = int(input("Enter a positive integer between 20 and 50:")) # asking user to enter an number and casting it to int

if myint < 20: # if myint is less than 20
    print(myint,"is less than the minimum acceptable value.") # print that it's too low
elif myint > 50: # else if my int is greater than 50
    print(myint,"is higher than maaximum acceptable value.") # print that it's too high 
else: # otherwise
    print(myint,"is within the acceptable range.") # print its within range
    result = myint**3 / 7.351 # algorithm for result
    print(result) # printing the result
    result2 = int (result) # casting result to int and assigning it
    print("The remainder obtained after dividing",myint,"by 5 =",result2) # print the result as an int
    print("The remainder obtained after dividing",myint,"by 5 =",myint%5) # printing the remainder