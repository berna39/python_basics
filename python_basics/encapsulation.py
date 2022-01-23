class Person:
    def __init__(self, name, age, gander):
        self.__name = name
        self.__age = age
        self.__gander = gander

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name



p = Person('Hashirama senji', 43, 'M')
#print(p.__age) this won't work