from datetime import date, datetime
import time


'''
Write a Python program to display the current date and time.
'''
print("Current date and time: ")

print(date.today())

print((datetime.now()).strftime("%I:%M %p"))