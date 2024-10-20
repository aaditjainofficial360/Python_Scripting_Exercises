"""
Template - Write a function value_sum(my_dict) that
returns the sum of the values in a dictionary
"""


def value_sum(my_dict):
    """
    Given a dictionary my_dict whose values are numbers, return 
    the sums of the values in my_dict
    """
    total_sum=0
    # Enter code here
    if len(my_dict)>0:
        for values in my_dict.values():
            total_sum+=values
    return total_sum


# Testing code
print(value_sum({}))
print(value_sum({0 : 1}))
print(value_sum({"Joe" : 1, "Scott" : 2, "John" : 4}))

# Output
#0
#1
#7
