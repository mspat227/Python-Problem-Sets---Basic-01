'''
24. Write a Python program to test whether a passed letter is a vowel or not. 
'''

letter = input("Letter: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u']

if letter in vowels:
    print("Vowel")
else:
    print("Not Vowel")