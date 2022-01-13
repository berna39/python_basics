from typing import cast


variale = 12

try:
    print("the value is " + variale)
except:
    print('Oops! something went wrong')


# other example
one = 'one'
two = 2

try:
    print(one/two)
except:
    print('Verify values')
finally:
    print('---- END ----')

f = 9
g = 'twig'

try:
    print(f / g) 
except TypeError:
    print('please everify the type of your valiables.')

try:
    print(12/ 0) 
except ZeroDivisionError:
    print('Impossible zero division.')

try:
    print(12/ k) 
except NameError:
    print('One of these valiables does not exist')

def birthYear():
    year = input() #user's entry
    try:
        y = int(year)
        if y <= 0:
            raise ValueError('Entrer a valid year please.')
    except ValueError:
        print('invalid data entry')

birthYear()
            

