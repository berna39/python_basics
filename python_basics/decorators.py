#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
from curses import wrapper
import numbers
import re


def upper_case_decorator(function):
    def wrapper():
        func = function()
        upper_case_format = func.upper()
        return upper_case_format

    return wrapper

def split_decorator(function):
    def wrapper():
        func = function()
        splited_format = func.split()
        return splited_format

    return wrapper

def sayHello():
    return 'hello world'

upper = upper_case_decorator(sayHello)
print(upper())


#------ decorator -------
@upper_case_decorator
def sayHi():
    return 'hi shango'

print(sayHi())

@split_decorator
def introduce():
    return 'my name is shango'

print(introduce())

@split_decorator #then this
@upper_case_decorator #these decorator will be executed first
def introduce():
    return 'my name is shango'

print(introduce())


#----- decorators with arguments -------
def decorator_with_arguments(function):
    def wrapper_expecting_args(arg_one, arg_two):
        print(f'my arguments are {arg_one} and {arg_two}')
        function(arg_one, arg_two)
    return wrapper_expecting_args

@decorator_with_arguments
def cities(one, two):
    print('the cities i like are {0} and {1}'.format(one, two))

cities('Nairobi', 'Accra')


# --- Defining General Purpose Decorators
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument(some_number):
    print("Arguments here is {0}".format(some_number))
function_with_no_argument(5)