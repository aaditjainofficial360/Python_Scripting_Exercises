"""
Template- Create a list zero_list consisting of 3 zeroes using a list comprehension
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

As a challenge, redo the previous problem using a nested list comprehension
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
"""

# Add code here for a list comprehension
zero_list=[ 0 for i in range(3)]

# Add code here for nested list comprehension
nested_list=[[0,0,0] for i in range(5)]


# Tests
print(zero_list)
print(nested_list)

# Output
#[0, 0, 0]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]