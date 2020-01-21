# comprehensions is valid for set , list , dictionary
# my_list = []
# for char in 'hello':
#     my_list.append(char)


# using list comprehension
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*3 for num in range(0, 40)]
my_list4 = [num*3 for num in range(0, 40) if num % 2 == 0]
print(my_list4)

# using set comprehension
my_set = {char for char in 'hello'}
print(my_set)

# for dictionary comprehension
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
my_dict2 = {key: key*2 for key in [1, 2, 3]}
print(my_dict2)
