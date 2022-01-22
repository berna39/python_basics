#For lazy execution

def my_generator(n):
    for  x in range(1, n):
        yield x ** 3

values = my_generator(10)

print(next(values))
print(next(values))
print(next(values))
print(next(values))

#getting the next value with iterators:

for x in values:
    print(x)
