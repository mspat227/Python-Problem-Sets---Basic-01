'''
Write a Python program that returns a string that is n (non-negative integer) copies of a given string
'''

n = abs(int(input("How many copies: ")))
word = input("What is the word: ")


for i in range(n):
    print(word)
