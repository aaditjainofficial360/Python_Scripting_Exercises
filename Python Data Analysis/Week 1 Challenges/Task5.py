"""
Solution - Write a function is_empty(my_dict) that
returns True if a dictionary is empty and False otherwise
"""


def is_empty(my_dict):
    """
    Given a dictionary my_dict, return True if the 
    dictionary is empty and False otherwise
    """
    
    # Enter code here
    if len(my_dict)==0:
        return True
    return False

# Testing code
print(is_empty({}))
print(is_empty({0 : 1}))
print(is_empty({"Joe" : 1, "Scott" : 2}))

# Output
#True
#False
#False
