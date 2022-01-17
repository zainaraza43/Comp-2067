# Zain Raza - Assignment 3 Question 1
# Comp 2067 - Winter 2022

def count_vowels(word) -> int: # helper function to count the number of vowels in a word and return the number of vowels

    counter = 0 # declaring a counter starting at 0
    word = word.upper() # force all the letter in word to upper
    vowels = ["A","E","I","O","U"] # list of all letters so that we don't have to make 4 or statements in the if statement

    for i in word: # for every letter in the word
        if i in vowels: # if that letter is in vowels list
            counter += 1 # add to counter
    
    return counter # return the counter

wordlist = ["hat", "book", "house", "flower", "tree", "grass", "cheetah", "lion", "tiger", "car", "boat"] # declaring a list of 10 strings

vowelFlag = False # a flag variable to see if a word had more than 3 vowels

for i in range(0, len(wordlist)-1, 3): # for loop starting at 0, goes to end of list, and counts by 3
    vowels = count_vowels(wordlist[i]) # counting the number of vowels by using the helper function and assigning it variable vowels

    print(wordlist[i],"contains",vowels,"vowel(s)") # printing the word and how many vowel it contains 

    if vowels >= 3: # if there are more than or equals to 3
        vowelFlag = True # set the vowelFlag = True
        break # break out of the loop

if vowelFlag: # if the flag was raised
    print("***Found string with 3 or more vowels!***") # print that there were 3 or more vowelse
else: # otherwise
    print("***Did not find suitable string.***") # print that it couldn't find a string with 3 or more vowels