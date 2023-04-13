'''
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''

amount = 10000
inter = 3.5
years = 7

total = amount + (inter * years * amount /100)

print(total)