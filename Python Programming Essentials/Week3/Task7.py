"""
Template - Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number):
    """This function prints the one's and ten's digit of the valid inputed number."""
    
    # Checking the number on validity of this function.
    if number>0 and number<100:
        ones_digit = number%10
        tens_digit = number//10

        message = "The tens digit is {}, and the ones digit is {}.".format(tens_digit,ones_digit)
    else:
        message = "Error: Input is not a two-digit number."
    # Printing the message
    print(message)
    return " "

###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.
