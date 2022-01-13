import string

basic_string = "Shikamaru"
print("Hello " + basic_string)

multiline_string = """frateli, d'italia,
l'italia se desta"""
print(multiline_string)

other_multiline_string = """other : frateli, d'italia,
l'italia se desta"""
print(other_multiline_string)

#string length
boo = "Toby"
print(len(boo))

for x in boo:
    print(x + "\n")

#checking if a word contains sth
sentence = "Joel is my friend and we work together"
if("Joel" in sentence):
    print("Joel is there")

other_sentence = "I'm a ninja, and i like coding Taijustu"
if("Python" not in other_sentence):
    print("No python there inside")

#slicing a string
country = "Hello Burkinafaso"
print(country[3:9])

#string transformation
my_name = " kalema shango joseph bernard  "
print(my_name.lower())
print(my_name.upper())
print(my_name.strip())

#string spliting
my_variable = "I Love God"
string_splited = my_variable.split(" ")
print(string_splited) 

#concatenate strings
first = "Hello,"
second = "World!"
print(first + " "+second)

#String format
age = 24
sentence = "Hello, i'm Toby and i'm {}"
print(sentence.format(age))

#with mutliple arguments
pi = 3.14
my_age = 24 
sentence = "Hello, i'm Toby and i'm {} and PI = {}"
print(sentence.format(my_age, pi))

#more class formatting
goal = 'steady rocking on the midnight train {}'.format('to zion')
print(goal)

destination = 'Zion'
same_goal = f'steady rocking on the midnight train to {destination}'
print(same_goal)

#all aplhabets in english
print(string.ascii_uppercase)


