import re

text = 'Hakuna matata Kenya'
#test if my text starts by Hakuna and ends by Kenya and return a matchobject
x = re.search('^Hakuna.*Kenya$', text)
print(x)