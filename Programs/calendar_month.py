# A programs that prints the calender of a month in a given year- Assignment 5.
# Batandwa Mgutsi
# 17/05/2020

import math
from math import floor


def day_of_week(day, month, year):
    """Returns the day of the week the given date falls. 1 is for Monday, 2 for Tuesday, etc.
       Uses Zeller's congruence algorithm @see https://en.wikipedia.org/wiki/Zeller%27s_congruence."""
    h = (day+floor(13*(month+1)/5)+year+floor(year/4) -
         floor(year/100)+floor(year/400)) % 7
    return ((h+5) % 7)+1


def is_leap(year):
    """Returns true if the given year is a leap year, false otherwise."""
    # Every year that is exactly divisible by four is a leap year, except for years that are
    # exactly divisible by 100, but these centurial years are leap years, if they are exactly
    # divisible by 400.
    # @see https://www.cse.unsw.edu.au/~cs1511/17s2/week02/09_leapYear/
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


def month_num(month_name):
    pass


def num_days_in(month_num, year):
    pass


def num_weeks(month_num, year):
    pass


def week(week_num, start_day, days_in_month):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
