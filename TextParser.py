'''
Author: Brendan Koning
Purpose: Frequency Analysis of a string
Date: January 20, 2014
Requirements: Text file containing only uppercase alphabetic characters, spaces are allowed, text file is named 'string.txt'
Output: A list of all alphabetic characters and their number of occurrences as well as percent of total characters
'''


file = ((open('string.txt', 'r')).read()); """Opens the text file with the string"""
file = file.replace(" ", ""); """Removes all spaces between words"""
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']; """Creates a list containing the alphabet"""
total = len(file) - file.count(' '); """Determines the total number of characters in the string"""

for i in letters:
    print (i + ' ' + str((file.count(i))) + '       ' +  str(round((file.count(i)/total * 100),2)) + '%');"""Counts the occurrence of each letter and prints it as well as the percentage of each letter"""
  
print ("Total" + ": " + str(total)); """Prints the total number of characters in the string"""