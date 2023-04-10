'''
 Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
'''
#importing calender module
import calendar

y = int(input("What is the year: "))
        
m = int(input("What is the month: "))


print(calendar.month(y, m))
