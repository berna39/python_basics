import re

text = 'Hakuna matata Kenya'
#test if my text starts by Hakuna and ends by Kenya and return a matchobject
x = re.search('^Hakuna.*Kenya$', text)
print(x)


# the [] is for a set of characters
other = 'Piaga kazi'
y = re.search('[x-z]', other)
print(y)

#the {} Exactly the specified number of occurrences
my_name = 'Shango'
print(re.search('Sha{2}go', my_name))

#the ^ represent starts with
band = 'Sauti sol'
print(re.search('^Sauti', band))

#the $ represent ends with
band = 'Sauti sol'
print(re.search('sol$', band))

#oops ! care about the caracter case
band = 'Sauti sol'
print(re.search('Sol$', band))

# the . represent any caracter
player = 'pogba'
print(re.search('p..ba', player))

# the * represents Zero or more occurrences (caracters)
print(re.search('p.*ba', player))

print(re.search('chat*', 'chateau'))


#replacing with regex
print(re.sub(r"(ab)", r" \1 ", "abcdef"))



