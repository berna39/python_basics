import random

# i seed 1 besauce random needs a number to start with, by default dandom uses the current system timestamp
random.seed(1)
print(random.random())

# we can  define a range to define random numbers
print(random.randrange(1, 9))
print(random.randrange(1, 9))
# i thinks it works the same as randrange
print(random.randint(9,19))

#we can make a choice randomly 
companies = ['google', 'facebook', 'amazon', 'apple', 'microsoft']
print(random.choice(companies))

fruits = ['orange', 'banana', 'apple', 'grandine']
random.shuffle(fruits)
print(fruits)

strickers = ['Vardy', 'Jota', 'Kane', 'Lukaku', 'Jimenez', 'Mahrez', 'Antonio', 'Woods', 'Pukki', 'Zaha', 'St Maximin', 'Salah', 'Christiano', 'Cavani', 'Daka', 'Saka']
random_stricker = random.choice(strickers)
print(random_stricker) #it was diogo jota ! lol

random_strickers = random.choices(strickers, k=3)
print(random_strickers) #it was diogo jota ! lol