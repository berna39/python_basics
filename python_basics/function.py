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

#advanced topic about functions
#python's functions are first class citizen

def plus_one(number):
    return number + 1

increment = plus_one #assigning a function to a variable
print(increment(2))

#definining a function into another
def process(number):
    print(f'the number passed is {number}')

    def increment(someting):
        return someting + 1
    
    result = increment(number)

    return result

print(process(3))

