'''   Instructions
Challenge: Optimize the function to handle large input numbers efficiently.
=====================================================
Description: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False
 otherwise'''

import math
from operator import truediv

#Define function
def is_prime(number: int) -> bool:
    print (f"the entered number {number} is a prime number")
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    limit = int(math.isqrt(number))
    print("Limit = ",limit)
    i = 5
    while i <= limit:
        print ("i= ", i)
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

print (is_prime(1103))

