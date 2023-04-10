'''
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import datetime

d1 = "2014-7-2"
d2 = "2014-7-11"


d1 = datetime.strptime(d1, "%Y-%m-%d")
d2 = datetime.strptime(d2, "%Y-%m-%d")
print(abs((d2 - d1).days))