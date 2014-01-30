'''
Author: Brendan Koning
Purpose: Apply a shift cipher of a user chosen amount to a string
Date: January 20, 2014
Requirements: Text file containing only uppercase alphabetic characters, commas, and periods, spaces are allowed, text file is named 'string.txt'
Output: A string with letters which are all shifted based on a user chosen amount

'''

file = (open('string.txt','r')).read(); """Opens the text file with the string"""
file = file.replace(',',''); """Removes all commas"""
file = file.replace('.',''); """Removes all periods"""
var = int(input("Choose shift amount: ")); """Takes user input for the shift amount"""

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']; """Creates a list of all capital alphabetic characters"""

for i in file:
    if(i != ' '):   
        plainLetter = letters.index(i); """Determines the index of the current letter in the string"""       
        cipherLetter = plainLetter + var; """Determines the index of the current letter after being shifted the user chosen amount"""
        print(letters[cipherLetter % 26], end='' ); """Prints the letter after it has been shifted"""
    else:
        print (' ', end=''); """If the character is a space, print a space and move on to the next character"""