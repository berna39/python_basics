one_set = {'suna', 'kumo', 'kiri'}
other_set = {'konoa', 'iwa'}

#joining two sets
print(one_set.union(other_set))

#adding ohter_set's element to one set
one_set.update(other_set)
print(one_set)

entreprises = { 'apple', 'microsoft', 'oracle', 'google', 'meta' }
fruits = { 'banana', 'orange', 'apple' }

inters = entreprises.intersection(fruits)
print(inters)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

f = { 'toto', 'koko', 'titi' }
g = { 'ngabulo', 'letudiant', 'kokumbo', 'toto', 'koko' }
h = f.symmetric_difference(g)

print(h)