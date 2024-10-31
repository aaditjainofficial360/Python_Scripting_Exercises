"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if (year>=datetime.MINYEAR and year<=datetime.MAXYEAR):
        if (month>=1 and month<=11):
            days = datetime.date(year,month+1,1)-datetime.date(year,month,1)
        elif month==12:
            days = datetime.date(year,12,1)-datetime.date(year,11,1)
        return days.days
    else:
        return 0

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if (year>=datetime.MINYEAR and year<=datetime.MAXYEAR) and (month>=1 and month<=12) and days_in_month(year,month):
        return True
    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2):
        days_difference = abs(datetime.date(year1,month1,day1)-datetime.date(year2,month2,day2))
        return days_difference.days
    return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year,month,day):
        birthday_date = datetime.date(year,month,day)
        today_date = datetime.date.today()
        if today_date>birthday_date:
            age_of_a_person = today_date-birthday_date
            return age_of_a_person.days
        else:
            return 0
    return 0

# Tests
# print( age_in_days(2016, 12, 31))
# print(age_in_days(2017, 1, 1))
# print(days_between(2014, 5, 5, 2014, 5, 6))
# print(days_in_month(1, 1))
# print(is_valid_date(9998, 12, 31))