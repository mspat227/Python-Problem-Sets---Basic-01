'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
'''

number = int(input("Number: "))

new_number = (number) + (number**2) + (number**3)

print(new_number)