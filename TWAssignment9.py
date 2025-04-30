'''Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.'''

# Input ask user to enter a character
char_input = input("Enter a single character: ")

# check to see that the input is 1 character long and is a letter
if len(char_input) == 1 and char_input.isalpha():
    # convert to lowercase
    char = char_input.lower()
    #Check for vowel or constant
    if char in 'aeiou':
        print("character is a vowel.")
    else:
        print("character is a constant.")

else:
    # Handle cases that are greater than 1 character
    if len(char_input) != 1:
        print ("Error: Please enter only one character!")
    else:
        print("Error: The character is not a letter!")
