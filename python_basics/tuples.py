#used to store multiple elements into one variable
my_tuple = ('kakashi', 'obito', 'rhin')
print(my_tuple)

my_other_tuple = ('toby', 'kabuto', 39, True)
print(my_other_tuple)

anoter_way_tupple = tuple(('code', 'pray', 'sleep', 'play'))
print(anoter_way_tupple)


#operations
testing_tuple = ('hashirama', 'tobirama', 'sarutoni', 'minato', 'tsunade', 'kakashi', 'naruto')

print(testing_tuple[1]) # access item
print(testing_tuple[-3]) # access item with reverse order
print(testing_tuple[1:4]) #range indexing
print(testing_tuple[-4:-1]) #range indexing with negative numbers
if 'kakashi' in testing_tuple: #testing if a tuple conains any value
    print('hello Sensei')


#tuple's values are inchangeable but we can convert it into a list and then convert it back to a tuple
my_list = list(testing_tuple)
my_list[0] = 'madara'
testing_tuple = tuple(my_list)
print(testing_tuple)

#adding sth to a tuple
my_list = list(testing_tuple)
my_list.append('terminator')
testing_tuple = tuple(my_list)
print(testing_tuple)


