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
    """Returns the number of a month, with January as month number 1"""
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]

    return months.index(month_name)+1


def num_days_in(month_num, year):
    """Returns the number of days in the given month inthe given year."""

    # Febrary has 28 days normally, and 29 in a leap year
    # April, June, September, Nov have 30 days
    # The rest have 31 days

    if month_num == 2:
        return 29 if is_leap(year) else 28
    if month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        return 30

    return 31


def num_weeks(month_num, year):
    """Returns the number of weeks spanned by the given week in the given month."""

    # The first and last weeks are the ones that may not have full days.
    weeks = 0
    remainigDays = num_days_in(month_num, year)

    missingDaysInFirstWeek = day_of_week(1, month_num, year) - 1
    daysInFirstWeek = 7 - missingDaysInFirstWeek
    weeks += 1
    remainigDays -= daysInFirstWeek

    fullWeeks = remainigDays // 7
    weeks += fullWeeks
    remainigDays -= (fullWeeks*7)

    # Now only the last weeks deyas remain
    if remainigDays > 0:
        weeks += 1

    return weeks


def add_leading_space(num):
    if num < 10:
        return f' {num}'
    return num


def week(week_num, start_day, days_in_month):
    """Returns a string consisting of the day of the month for each day in that
    week, starting with Monday and ending with Sunday."""

    # Number of days missing should be changed from zero only if week_num is 1
    numberOfDaysMissing = start_day-1 if week_num == 1 else 0

    # For week 1 the start date is always the 1st of the month
    # For subsequent weeks, the start date is always on a Monday
    startDate = 1

    if week_num > 1:
        # Starting from the 2nd day and iterate until we have encountered
        # week_num Mondays, the week_numth Monday is the start date for the week.

        # Set initial value to 1 to skip week 1
        weekCount = 1
        day = start_day + 1
        for date in range(2, days_in_month+1):
            if day > 7:
                day = 1
            if day == 1:
                weekCount += 1
                if weekCount == week_num:
                    startDate = date
                    break
            day += 1

    # Render the line
    # The first week should be padded with 2 spaces for every missing day.
    line = ''.rjust(numberOfDaysMissing*2)
    for iii in range(0-numberOfDaysMissing, 6-numberOfDaysMissing+1):
        if(iii < 0) or (startDate+iii > days_in_month):
            continue
        else:
            line += f'{add_leading_space(startDate+iii)} '

    # Ignore the last space
    return line[0:len(line)-1]


def main():
    pass


if __name__ == '__main__':
    main()
