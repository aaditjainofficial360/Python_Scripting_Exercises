"""
Template - Compute whether a person is cool.
"""

###################################################
# Is cool formula
# Student should enter function on the next lines.

def is_cool(name):
    '''This function matches the inputed name to a list of names.'''

    if name in ["Joe","John","Stephen"]:
        return True
    else:
        return False


###################################################
# Tests
# Student should not change this code.

name = "Joe"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

name = "John"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Stephen"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Scott"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.
