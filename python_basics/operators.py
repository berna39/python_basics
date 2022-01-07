#Arithmetic operations
x = 21
y = 7

print(x+y) #addition
print(x-y) #substraction
print(x*y) #multiplication
print(x/y) #division
print(x**y) #addition
print(x//y) #Floor division

#assignment operator
number = 0

number += 5 #same as number = number + 5
number -= 5 #same as number = number - 5
number *= 5 #same as number = number * 5
number **= 5 #same as number = number ** 5
number /= 5 #same as number = number / 5
number //= 5 #same as number = number // 5

#logical operations
age = 18
gander = 'm'

if age >= 18 and gander == 'm':
    print("hello adult man")


country = 'Belgium'
if country == 'DRC' or country == 'Kenya':
    print('I\'m home')
else:
    print('Hello stranger')


o = "Stromae"
p = o
q = "Stromae"

if o is p:
    print('o is p')

if o is q:
    print('o is q')
else:
    print('o is not q')





