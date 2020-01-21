# map ,filter ,zip ,and reduce
from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(li):
    return li * 2


# print(list(map(multiply_by2, my_list)))
# print(my_list)
# map calls the function so no need to pass anything
# map runs and loops all the items and performs function on each item
# map is a pure function so it does not change my_list istead it creates a copy

# filter
def only_odd(item):
    return item % 2 != 0


# print(list(filter(only_odd, my_list)))
# print(my_list)
# it filters according to the condition given if true then add else do not add if false

# zip

# print(list(zip(my_list, your_list)))
# print(my_list)


# it zips together multiple iterators in form of a Tuple

# Reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
print(my_list)
# reduce adds the acc to item and then it updates the acc with the sum until iterator reaches end
