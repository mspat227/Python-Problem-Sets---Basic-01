'''
Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''
#get the number
number = int(input("What is the number: "))

if abs(number - 1000) <= 100 or abs(number - 2000) <= 100:
    print(f"{number} near to 1000 or 2000")
else:
    print(f"{number} not near to 1000 or 2000")
