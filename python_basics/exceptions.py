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


