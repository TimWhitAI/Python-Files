'''Challenge: Handle negative exponents efficiently.
====================================
Description: Develop a function named power that takes two integers, base and exponent, as input and returns base
raised to the power of exponent.'''



# Define the Function
def power(base,exponent) -> int:
    if exponent < 0: #Handle negative exponents efficiently by dividing 1 by the absolute value of number
        rec_base = 1 / base
        abs_exp = abs(exponent)
        result = rec_base ** abs_exp
    else:
        result = base ** exponent
    return result

#Enter base and exponent
input_base = int( input("enter the base: "))
input_exponent = int(input("enter the exponent: "))
#Call function and print the results
print (power(input_base,input_exponent))
