'''
23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is less than 2.
'''

number = abs(int(input("Number of coppies: ")))

word = input("Word: ")

if len(word) > 2:
    word = word[0] + word[1]


print(word * number)