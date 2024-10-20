"""
Template - Write a function make_dict(key_value_list) that
takes a list of tuples (key, value) and returns a 
dictionary with these keys and values
"""


def make_dict(key_value_list):
    """
    Given a list of tuples of the form (key, value), 
    return a dictionary with the corresponding keys and values
    """
    result_dictionary={}
    # Enter code here
    if len(key_value_list)>0:
        for item in key_value_list:
            result_dictionary=dict(item)
    return result_dictionary

# Testing code
print(make_dict([]))
print(make_dict([(0, 1)]))
print(make_dict([("Joe", 1), ("Scott", 2), ("John", 4)]))

# Output
#{}
#{0: 1}
#{'John': 4, 'Joe': 1, 'Scott': 2}
