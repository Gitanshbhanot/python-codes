my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)  # brings cursor back to desired point
# print(my_file.read())
# print(my_file.readline())  # print only 1 line
print(my_file.readlines())  # makes list of all lines in file
my_file.close()
