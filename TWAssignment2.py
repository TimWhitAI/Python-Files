'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''

#Input

try:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
#Process
    assert length > 0 and width > 0, "Cannot determine area, length and width must be positive"
    area = length * width
    print("The area of the rectangle is: ", area)
except AssertionError as msg:
   print(msg)

