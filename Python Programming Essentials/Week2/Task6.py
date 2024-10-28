"""
Template - Compute the area of a circle, given the length of its radius.
"""

# Import the math module to access the exact value of pi
import math
PI = math.pi

###################################################
# Circle area formula
# Student should enter function on the next lines.

def circle_area(radius):
    '''This function calculates the area of the circle by its radius.
    The Area of Circle is given by its formula :

        Area = PI * Radius * Radius
    '''
    area = PI*radius*radius
    return area


###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has an area of 201.06192983 square inches.
#A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
#A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.
