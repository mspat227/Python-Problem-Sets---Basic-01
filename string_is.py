'''
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is".
'''
string = input("What is the word? ")

if len(string) > 2 and string[0] == "I" and string[1] == "s":
    #if len(text) >= 2 and text [:2] == "Is": <also correct>
    print(string)
else:
    print('Is' + string)