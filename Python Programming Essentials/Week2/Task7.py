"""
Template - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula
# Student should enter function on the next lines.

def future_value(present_value,annual_rate,years):
    '''This function calculates the future value from its present value 
    by compounding at its annual rate yearly'''

    future_value = present_value*(1+annual_rate/100)**years
    return future_value


###################################################
# Tests
# Student should not change this code.


present_value, annual_rate, years = 1000, 7, 10	
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")
    
present_value, annual_rate, years = 200, 4, 5
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")

present_value, annual_rate, years = 1000, 3, 20
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.
