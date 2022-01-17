# Zain Raza - Assignment 3 Question 3
# Comp 2067 - Winter 2022

def fibonacci(x) -> list: # function that will generate x fibonacci numbers
    
    fib = [] # declaration of an empty list 

    if x >= 1: # if the user wants at least 1 element
        fib.append(0) # append the first element, 0
    else:
        return fib # if the user wants less than 1 element, return an empty list
    if x >= 2: # if the user wants at least 2 elements
        fib.append(1) # append the second element, 1
    
    for i in range(1, x-1): # going from the 2nd element on
        fib.append(fib[i] + fib[i-1]) # add the addition of the last 2 elements of the list
    
    return fib # return the completed list

x = 20 # declaring a variable x that will be the number of elements fibonacci returns

print("The first",x,"Fibonacci numbers are:",fibonacci(x)) # printing the first 20 elements of the fibonacci sequence