basic_string = "Shikamaru"
print("Hello "+basic_string)

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
    print(x+"\n")

#checking if a word contains sth
sentence = "Joel is my friend and we work together"
if("Joel" in sentence):
    print("Joel is there")

other_sentence = "I'm a ninja, and i like coding Taijustu"
if("Python" not in other_sentence):
    print("No python there inside")