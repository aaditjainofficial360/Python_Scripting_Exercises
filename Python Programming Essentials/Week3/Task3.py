"""
Template - Compute whether the given time is lunchtime.
"""

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.

def is_lunchtime(hour,is_am):
    '''This function checks the lunch time. The Lunch time is 11 AM or 12 PM.'''

    if is_am:
        if hour==11:
            return True 
        else:
            return False
    else:
        if hour==12:
            return True
        else:
            return False



###################################################
# Tests
# Student should not change this code.

def is_lunchtime_test(hour, is_am):
    """Tests the is_lunchtime function."""
    print(hour, end = "")
    if is_am:
        print("AM", end = "")
    else:
        print("PM", end = "")
    if is_lunchtime(hour, is_am):
        print(" is lunchtime.")
    else:
        print(" is not lunchtime.")

is_lunchtime_test(11, True)
is_lunchtime_test(12, True)
is_lunchtime_test(11, False)
is_lunchtime_test(12, False)
is_lunchtime_test(10, False)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.
