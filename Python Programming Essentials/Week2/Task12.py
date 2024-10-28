"""
Template - Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number):
    '''This function prints the digits at one's and ten's place. '''

    ones_digit = number%10
    tens_digit = number//10

    output = "The tens digit is {}, and the ones digit is {}.".format(tens_digit,ones_digit)
    print(output)
    return " "
    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
