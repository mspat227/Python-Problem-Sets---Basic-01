'''
Write a Python program that calculates the area of a circle based on the radius entered by the user.
A = \pi r^2

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

'''

radius = float(input("What is the radius? ").strip())

area = (radius * radius) * 3.14

print("Area:" ,area)
