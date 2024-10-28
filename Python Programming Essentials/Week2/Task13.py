"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    '''This function generates the Powerball number through a list of randomly generated numbers'''
    
    list_of_five = random.sample(range(1,60),5)
    powerball_number = random.choice(range(1,36))
    
    message = "Today's numbers are {}, {}, {}, {}, and {}. The Powerball number is {}.".format(list_of_five[0],list_of_five[1],list_of_five[2],list_of_five[3],list_of_five[4],powerball_number)
    print(message)
    return " "
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.
