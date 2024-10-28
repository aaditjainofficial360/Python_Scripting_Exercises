"""
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.

def total_seconds(hours,minutes,seconds):
    '''This function takes hours, minutes and seconds as an input parameter and calculates total seconds using
    formula 
    seconds = hours*3600 + minutes*60 + seconds
    '''
    return hours*3600+minutes*60+seconds


###################################################
# Tests
# Student should not change this code.

hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.