"""
Template - Compute the area of a rectangle, given its width and height.
"""

###################################################
# Rectangle area formula
# Student should enter function on the next lines.

def rectangle_area(width,height):
    '''This function takes width and height of rectangle as a parameter
        and outputs the area of rectangle. The Area of Rectangle is the product
        of width and height of rectangle.'''
    
    area = width * height
    return area


###################################################
# Tests
# Student should not change this code.

width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.
