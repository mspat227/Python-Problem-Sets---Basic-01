'''
41. Write a Python program to check whether a file exists.
os.path.isfile()  also 
'''

import os


if os.path.exists('hello.txt'):
    print('Yes')