# lambda functions

from functools import reduce

# my_list = [1, 2, 3]


# def multiply_by2(item): no need for function now bcos of lambda
#     return item*2


# print(list(map(lambda item: item*2, my_list)))
# print(list(filter(lambda item: item%2 != 0, my_list)))
# print(reduce(lambda acc, item: acc+item, my_list))
# print(my_list)
# lambda expression perform actions which the computer forgets about

# square the list
my_list = [5, 4, 3]

print(list(map(lambda item: item*item, my_list)))

# list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
