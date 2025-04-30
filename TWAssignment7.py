'''Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.
===============================================
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.'''

# Input
year_input = input("Enter a year: ")

if year_input.isdigit():
    year = int(year_input)
    # ensure year is positive
    if year > 0:
        remainder4 = year % 4
        remainder100 = year % 100
        remainder400 = year % 400
        if remainder4 == 0:
            if remainder100 == 0:
                if remainder400 == 0:
                    print(f"{year} is a leap year.")
                else:
                    print(f"{year} is NOT a leap year.")
            else:
                print(f"{year} is a leap year.")
        else:
            print(f"{year} is NOT a leap year.")
    else:
        print(f"{year} is not a valid year.")
else:
    print(f"{year_input} is not a valid year.")



