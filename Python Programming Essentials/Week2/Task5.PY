"""
Template - Compute the circumference of a circle, given the length of its radius.
"""

import math
PI = math.pi

###################################################
# Circle circumference formula
# Student should enter function on the next lines.

def circle_circumference(radius):
    '''This function calculates the circumference of the circle from its radius.
    The Circumference of the circle is given by the formula 
        Circumference = 2 * PI * radius
    '''

    circumference = 2*PI*radius
    return circumference

###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
#A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
#A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.
