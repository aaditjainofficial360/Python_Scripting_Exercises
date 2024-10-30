"""
Template - Compute the smaller root of a quadratic equation.
"""

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.

def smaller_root(a,b,c):
    '''This function takes the cofficients of x^2, x and constant in a quadratic equation
        and computes the smaller root of the equation, if root exists.'''
    
    # Calculating the discriminant
    discriminant = ((b**2)-(4*a*c))**0.5
    
    # Two Real Roots
    if str(discriminant)>'0':
        root = min((-b-discriminant)/(2*a),(-b+discriminant)/(2*a))
    # One Real Root
    elif str(discriminant)=='0':
        root = (-b+discriminant)/(2*a)
    # No Real Roots
    else:
        message = "Error: No real solutions"
        return message
    return root



###################################################
# Tests
# Student should not change this code.

coeff_a, coeff_b, coeff_c = 1, 2, 3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2, 0, -10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None
