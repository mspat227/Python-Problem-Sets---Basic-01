'''
 Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

Sample data : 3, 5, 7, 23
'''
sample_data = "3, 5, 7, 23"

my_list = sample_data.split(",")

my_tuple = tuple(my_list)


print("List: ", my_list)
print("Tuple: ", my_tuple)