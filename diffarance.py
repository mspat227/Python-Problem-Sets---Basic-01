'''
35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5
'''
x = int(input("X: "))
y = int(input("Y: "))

if x == y or x + y == 5 or abs(x - y) == 5:
    print("True")
else:
    print("False")