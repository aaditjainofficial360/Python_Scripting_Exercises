"""
Template - Compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Distance formula
# Student should enter function on the next lines.

# Hint: You need to use the power operation ** .

def point_distance(x_0,y_0,x_1,y_1):
    '''This function calculates the distance between two points on a cartesian plane.
        It used distance formula. '''
    
    distance_formula=((y_0-y_1)**2 + (x_0-x_1)**2)**0.5
    return distance_formula

###################################################
# Tests
# Student should not change this code.


x_0, y_0, x_1, y_1 = 2, 2, 5, 6
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 1, 1, 2, 2
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 0, 0, 3, 4
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The distance from (2, 2) to (5, 6) is 5.0.
#The distance from (1, 1) to (2, 2) is 1.41421356237.
#The distance from (0, 0) to (3, 4) is 5.0.
