'''
34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
'''
number1 = int(input("Number1: "))
number2 = int(input("Number2: "))

sum = number1 + number2

if 15 <= sum <= 20:
    print("Sum: 20")
else:
    print("Sum: ", sum)