'''
33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
'''

numbers = []

while len(numbers) < 3:
    x = int(input("Number: "))
    numbers.append(x)

if numbers[0] == numbers[1] or numbers[1] ==numbers[2] or numbers[0] == numbers[2]:
    print("Sum: 0")
else:
    sum = numbers[0] + numbers[1] + numbers[2]
    print("Sum: ", sum)   