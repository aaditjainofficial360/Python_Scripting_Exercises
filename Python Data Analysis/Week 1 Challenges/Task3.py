"""
Template - Add the specified key/value pair to an
existing dictionary my_dict
"""

# Initialize dictionary
my_dict = {"Joe" : 1, "Scott" : 2}

# Add key/value pair "John" : 3
my_dict["John"]=3


# Tests
print(type(my_dict))
print(my_dict["Joe"])
print(my_dict["Scott"])
print(my_dict["John"])
print(my_dict)

# Output - note that order of key/values pairs in output is unimportant
#<class 'dict'>
#1
#2
#3
#{'Scott': 2, 'John': 3, 'Joe': 1}