#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
def upper_case_decorator(function):
    def wrapper():
        func = function()
        upper_case_format = func.upper()
        return upper_case_format

    return wrapper


def sayHello():
    return 'hello world'

upper = upper_case_decorator(sayHello)
print(upper())