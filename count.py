'''
22. Write a Python program to count the number 4 in a given list.
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 6, 4, 5, 78, 56, 21, 4, 4, 6, 8, 45, 65, 54, 4]

counter = 0

for i in range(len(my_list)):
    if my_list[i] == 4:
        counter +=1
    else:
        pass

print(counter)