'''Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.
=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.'''


#Input number of rows for the triangle
num_of_rows = input("Enter the number of rows for the Triangle: ")



while True: # make sure a valid number is entered
    if num_of_rows.isdigit():
        number = int(num_of_rows)

        if number > 0:
            break
        else:
            user_input = input("The number must be a positive number. Please try again: ")
            num_of_rows = user_input
    else:
        user_input = input("Invalid number. Please enter a positive number: ")
        num_of_rows = user_input

symbol_input = input ("Enter the symbol you wish to use to create Triangle: ")

i = 1
while i <= number: #Loop to build triangle
    repeat_symbol = symbol_input * i
    print(repeat_symbol)
    i = i + 1

