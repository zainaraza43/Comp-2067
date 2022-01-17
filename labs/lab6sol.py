# Zain Raza - Lab 6
# Comp 2067 - Winter 2022

def multiply_lists(list1, list2) -> list: # takes two lists and returns a list with multiplied products

    print("list1 =",list1,";    list2 =",list2)

    products = [] # declare empty products list

    for x in list1: # for every element in list1
        for y in list2: # for every element in list2
            products.append(x * y) # add the product of the current 2 elements

    return products # return the end products list

list1 = [4, 2, 7] # declare list1
list2 = [3, 1, 9, 2] # declare list2

prod_list = multiply_lists(list1, list2) # declare prod_list as a function taking in list1 and list2

print("prod_list =",prod_list) # printing prod_list

print("sum =", sum(prod_list)) # printing the summation of all elements in prod_list

print("Number of occurrences of 4 is:",prod_list.count(4)) # printing the number of occurences of the number 4 in prod_list

print("72 is in prod_list:",72 in prod_list) # printing if 72 is in prod_list

print(prod_list) # printing the sorted list ???  