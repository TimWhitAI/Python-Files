'''
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''

#Prompt user to enter principle amount
prinicpal = float(input("Enter principal amount: "))

#Prompt user to enter Interest rate
Intrate = float(input("Enter Interest Rate in percentage: "))

#Prompt user to enter Interest rate
timePeriod = float(input("Enter Time Period in years: "))

#Process formula
SimpleIntr = (prinicpal * Intrate * timePeriod) / 100

#Display calculated Simple  Interest
print("The simple Interest id: ", SimpleIntr)