addition = lambda a, b : a + b

print(addition(12,1))

def multiplyer(by):
    return lambda number: number * by

my_function = multiplyer(2)
print(my_function(5))