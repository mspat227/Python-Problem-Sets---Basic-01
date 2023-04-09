'''
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

.title() will capitalaized the forst letter
'''


first = input("First Name: ").title()
last = input("Last Name: ").title()

print(f"{last} {first}")