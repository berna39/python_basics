def sayHello():
    print('Hello world !')

def addition(a, b):
    return a + b

#if we don't how much parameters will be passed
def buy_cars(*cars):
    print('i buy ' + cars[2])

#default parameter value
def say_country(country = 'Kenya'):
    print('My country is ' + country)

sayHello()

sum = addition(12, 8)
print(str(sum))

buy_cars('volvo', 'toyota', 'honda', 'mercedes')

say_country('DRC')