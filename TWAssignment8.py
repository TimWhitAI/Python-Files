'''Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.'''

# Input
sub1_input = input("Enter the numeric grade for subject 1: ")
sub2_input = input("Enter the numeric grade for subject 2: ")
sub3_input = input("Enter the numeric grade for subject 3: ")


subject1 = int(sub1_input)
subject2 = int(sub2_input)
subject3 = int(sub3_input)

# process

average = (subject1 + subject2 + subject3) / 3
if average > 89:
    print(f"The average grade is {average} giving you an A.")
elif 79 < average < 90:
    print(f"The average grade is {average} giving you an B.")
elif 69 < average < 80:
    print(f"The average grade is {average} giving you an C.")
elif 59 < average < 70:
    print(f"The average grade is {average} giving you an D.")
else:
    print(f"The average grade is {average} giving you an F.")
