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


#class creation instance
p = Person('Kabuto Yakushi', 'm')
print(p.gander)

#basic method call
p.sayHello()
