class Car:
    mark = ''
    model = ''

    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
    
    def drive(self):
        print('i drive ' + self.model + ' - ' + self.mark)
    
    def vruum(selft):
        print('vrouuuuum')

    def other(self):
        pass

car = Car('Ford', 'Mustang')
car.drive()
car.other()