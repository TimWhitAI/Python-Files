'''Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.'''
try:
#input
    hours_input =float(input("Enter time in duration of hours: "))

#Process
    assert hours_input > 0, "Hours must be a positive number"
    minutes = int(hours_input * 60)
    seconds = int(hours_input * 3600)
# output
    print("The hours represented in minutes is: ", minutes)
    print("The hours represented in seconds is: ", seconds)
except AssertionError as msg:
   print(msg)



