'''
7. Write a Python program to count the number of each character in a text file
'''
#open the file and read the file to a var
file = open("hello.txt", "r")
my_string = file.read()

charactor_count = []
charactors = []

#append the charactors in to a list
for i in range(len(my_string)):
    charactors.append(my_string[i])

#append the charactor count to list
for i in range(len(my_string)):
    charactor_count.append(my_string.count(my_string[i]))

print(str(list(zip(charactors, charactor_count))))

#can use the collections module