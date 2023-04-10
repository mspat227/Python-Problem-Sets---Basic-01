'''
 Write a Python program to get the volume of a sphere with radius six.
'''
import math 

radius = float(input("What is radius of the saphere? "))

volume = (4/3) * math.pi * (radius**3)

print(f"Volume of a {radius} radius sphere is {volume}")