my_set = { 'zidane', 'rivaldo', 'figo', 'owen', 'ronaldo', 'pavel nedved', 'chevchenko', 'ronaldinho', 'carnavaro', 'kaka' }

#to copy a set
clone_set = my_set.copy()
print(clone_set)

#the difference between two sets
my_set_bis = { 'zidane', 'rivaldo', 'figo', 'owen', 'ronaldo', 'pavel nedved', 'chevchenko', 'eto\'o', 'carnavaro', 'kaka' }
print(my_set.difference(my_set_bis))

#remove an element from set
my_set.discard('carnavaro')
print(my_set)

my_set.pop()
print(my_set)