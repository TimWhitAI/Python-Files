'''Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other
 sequence of characters that reads the same forward and backward.'''

#Input prompt user to enter a string
string_input = input("Enter a string of characters: ")

#Create a reversed version of string
string = string_input
reversed_string = string[::-1]

length = len(string)
palindrome = True
for i in range(length): #Compare each character of the two strings
    if string[i] == reversed_string[i]:
        continue
    else:
        palindrome = False
        break

if palindrome:
    print (string, "is a palindrone") #if all characters match
else:
    print (string, "is NOT a palindrone")#if a character does not match
