class Panda:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 50
    
    def __str__(self):
        return f'name = {self.name}, age = {self.age}, hunger = {self.hunger}'

    def eat(self, food_points):
        if self.hunger >= 100:
            print(f'{self.name} a déjà bien mangé')
        else:
            self.hunger += food_points
            if self.hunger >= 100:
                print('Est rassasié')
                self.hunger = 100
        print(f'{self.name} vient de magers')
