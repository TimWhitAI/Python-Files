'''Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.'''

#input
weight_input = input("Enter your weight in in kilograms: ")
height_input = input("Enter your height in meters: ")
weight = float(weight_input)
height = float(height_input)

#Process BMI
BMI_results = (weight/ (height**2))
print("The BMI is: ", BMI_results)
if BMI_results < 18.5:
    print("You are underweight")
if BMI_results > 18.5 and BMI_results < 24.9:
    print("Your weight is normal")
if BMI_results > 24.9:
    print("You are overweight")