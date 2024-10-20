"""
Template - Select a specific item in a nested list
"""

# Define a nested list of lists
nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]
print(nested_list)

# Add code to print out the item in this nested list with value 7
for item in nested_list:
    if 7 in item:
        for j in item:
            if j==7:
                print(j)
# Output
#[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
#7