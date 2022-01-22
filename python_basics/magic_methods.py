from os import name


class Team:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self) -> str: #the str magic method for object details as string
        return f'name : {self.name}, country : {self.country}'

    def __del__(self): #this will be called once the object is destroyed
        print('The object has been destroyed')

team = Team('liecester', 'England')
print(team)


#-------- the __add__ magic method #

#the problem
class Vector:
    def __init__(self, a, b):
        self.a = a 
        self.b = b

v1 = Vector(3, 5)
v2 = Vector(4, 8)
# v3 = v1 + v2 # this would return a typeError Exception
        