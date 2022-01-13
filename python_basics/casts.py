#casting types

from typing import Literal


a  = 12
float_casted = float(a)
print(float_casted)

b = 6
string_casted = str(b)
print(type(string_casted))

my_tuple = ('tom', 'alice')
list_squad = list(my_tuple)
print( 'the squad is : '+ ' & '.join(list_squad))