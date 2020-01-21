# HOC
# functions which accept a function
# for ex: map(), filter(), reduce(), set()


def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func
