'''
1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

'''
#when convert to set there will be no duplicates in number sequence
# so the length of two variables will be differnt
def same(n):
    if len(n) == len(set(n)):
        print("no same numbers")
    else:
        print("same numbers included")

