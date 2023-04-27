'''
6. Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word.
'''

my_string = "If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways."


my_list = my_string.split()

word_count = []

for i in range(len(my_list)):
    word_count.append(my_list.count(my_list[i]))

print(str(list(zip(my_list,word_count))))

'''
we can use list comprihention as below

word_count = [my_list.count(n)for n in my_list]

zip function can take two lists and add two as one but to display data you have to convert it to tuple, list or string
'''

