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
    print(one+two)
except:
    print('Verify values')
finally:
    print('---- END ----')