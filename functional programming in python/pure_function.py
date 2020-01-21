# rules for pure function
# 1 should give same output for same values
# 2 shouldn't have side effects


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


# if above function has print in it then it is not pure.
# if new_list is made global then the func. interacts with outside enviornment so it is not a pure func.

print(multiply_by2([1, 2, 3]))
