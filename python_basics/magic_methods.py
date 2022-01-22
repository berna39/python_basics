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