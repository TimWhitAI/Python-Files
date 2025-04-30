'''Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency
'''


#Input
amount_input =float(input("Enter amount: "))
currency_input = input("Enter currency of amount (e.g., USD): ")
exchange_input = input("Enter currency you would like to exchange for (e.g., EUR): ")
Currdict = {
"USD" : 0.90, #USA
"EUR" : 0.878638, #Euro
"GBP" : 0.751077, #Britian
"AUD" :	1.561533, #Austrailia
"CAD" :	1.386237, #Canada
"CHF" :	0.827964, #Swiss
"JPY" :	143.658861, #Japan
"CNY" :	7.286629 #China
}
#Process
exchange_rate = Currdict.get(exchange_input)
Conv_amount = amount_input * exchange_rate
print("The amount converted is: ", Conv_amount, exchange_input)
