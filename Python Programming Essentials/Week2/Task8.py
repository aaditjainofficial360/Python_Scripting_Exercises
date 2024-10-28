"""
Template - Compute a name tag, given the first and last name.
"""

###################################################
# Name tag formula
# Student should enter function on the next lines.

def name_tag(first_name,last_name):
    '''This function prints the firstname along with lastname'''

    combined = first_name+" "+last_name

    return "My name is "+combined

    
###################################################
# Tests
# Student should not change this code.
    
    
first_name, last_name = "Joe", "Warren"
print(name_tag(first_name, last_name))

first_name, last_name = "Scott", "Rixner"
print(name_tag(first_name, last_name))

first_name, last_name = "John", "Greiner"
print(name_tag(first_name, last_name))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.
#My name is Scott Rixner.
#My name is John Greiner.
