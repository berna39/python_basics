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

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, age):
        self.__age = age

    @property
    def Gander(self):
        return self.__gander

    @Age.setter
    def Age(self, gander):
        self.__gander = gander



p = Person('Hashirama senji', 43, 'M')
print(p.Name)
print(p.Age)
print(p.Gander)