#for loops
for x in range(1,9):
    print(x)


#for loop for slicing list
my_list = ['toto', 'tobi', 'terminator']

for person in my_list:
    print(person)


#for loop with else
for i in range(5):
    print(i)
else:
    print('finished')

#for loop with break

for i in range(6):
    if i == 3 : break
    print(i)

print('---- while loops ----')
y = 6
while y > 0:
    print(y)
    y -= 1