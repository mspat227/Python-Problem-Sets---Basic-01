'''
Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.
'''
#get the number
number = int(input("What is the number? "))

if number <= 17:
    answer = 17 - number
    print(answer)
else:
    answer = 2 * (number - 17) 
    print(answer)
