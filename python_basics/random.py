import random

# i seed 1 besauce random needs a number to start with, by default dandom uses the current system timestamp
random.seed(1)
print(random.random())

# we can  define a range to define random numbers
print(random.randrange(1, 9))
print(random.randrange(1, 9))

#we can make a choice randomly 
companies = ['google', 'facebook', 'amazon', 'apple', 'microsoft']
print(random.choice(companies))