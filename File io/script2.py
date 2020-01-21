with open('test.txt', mode='a') as my_file:  # it closes file automatically
    text = my_file.write('hey it\'s me!')
    print(text)
    print(f'the file consists of {my_file.readlines()}')
