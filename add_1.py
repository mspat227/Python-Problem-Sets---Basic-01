'''
36. Write a Python program to add two objects if both objects are integers. 
'''
x = input("X: ")
y = input("Y: ")

if x.isdigit() and y.isdigit():
    z = int(x) + int(y)
    print(z)
else:
    print("not integers")
