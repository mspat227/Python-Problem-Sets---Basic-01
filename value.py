'''
25. Write a Python program that checks whether a specified value is contained within a group of values.
'''

number = int(input("Number: "))

list_01 = [21,54,65,874,65,54,87,65,1,584,65,32,645,98,65,321,54,9,652,541,654,874,542,654,874,541,6854,521]


if number in list_01:
    print("True")
else:
    print("False")