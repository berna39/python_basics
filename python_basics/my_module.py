#this is a function defined to module
from mimetypes import init


def sayHello(name):
    print('Hello ' + name)

def addition(number_one, number_two):
    print('the dum of ' + str(number_one) + ' and ' + str(number_two) + ' is ' + str(number_one + number_two))

class Movie:
    def __init__(self, title):
        self.title = title
    
    def __str__(self) -> str:
        return f'title : {self.title}'
