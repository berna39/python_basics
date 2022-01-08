import json

my_json = '{"name": "Shango", "age": 24, "is_vaccined": "yes"}'

t = json.loads(my_json) #convert to json

print(t['is_vaccined']) # access to a key


# converting a python dict to a json
person = {
    "name": "Shango",
    "age": 23,
    "is_vaccined": "yes"
}

print(person) #here we'll have a python object (dict)
print(type(person))

converted = json.dumps(person) #converting to a string json

print(converted)
print(type(converted))

more_complet = {
  "name": "Shango",
  "age": 23,
  "married": False,
  "divorced": False,
  "brothers": ("King", "Joe", "Luk", "Yus", "Lil"),
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(more_complet, indent=4))