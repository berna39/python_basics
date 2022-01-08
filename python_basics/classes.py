class Person:
    name = 'shango'
    gander = 'm'
    #contrucctor
    def __init__(self, name, gander):
        self.name = name
        self.gander = gander

    #a basic method
    def sayHello(self):
        print('Hello there from ' + self.name)

#as class cannot be empty we put pass keyword
class Empty:
    pass

#class creation instance
p = Person('Kabuto Yakushi', 'm')
print(p.gander)

#basic method call
p.sayHello()

