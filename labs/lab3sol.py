# Zain Raza - Lab 3
# Comp 2067 - Winter 2022

list1 = ['windsor', 'toronto', 'ottawa', 'montreal', 'vancouver'] # defining list1

print("list1=",list1) # printing list1

print("The last 3 characters of the first element of list1 are:",list1[0][4:]) # printing the last 3 characters of the first element

cityname = input("Enter the name of a city in lowercase: ") # user input for a city

print("cityname =",cityname.upper()) # printing the name of the city 

list1.append(cityname) # adding cityname to list

print("The updated list1 after appending item is:",list1) # printing list1

print("min value of list1 is:",min(list1)) # printing min value of list1

list1[list1.index(min(list1))] = "minval" # assigning the string 'minval' to the minimum value in list1

print("The updated list1 after replacing item is",list1) # printing list1

year = int(input("Enter your year of birth (yyyy):")) # asking user for birth year and casting it to an int

sum = len(list1) + year # adding length of list to year

print("Number of elements in list1 is:", len(list1)) # number of items in list1

print("sum =",sum) # printing sum