values = ['Meschack', 'Shadrack', 'abedNego']

for x in values: #nirmal loop
    print(x)

#now let try to print also the index of of each element

index = 0 
for x in values: #nirmal loop
    print(index, x)
    index += 1

#Another common way to approach this problem is to use range() combined with len() 
# to create an index automatically. This way, you don’t need to remember to update the index

for index in range(len(values)):
    print(index, values[index])


print(index) # With this example, one common bug that can occur is when you forget to update value at the beginning of 
             #  each iteration. This is similar to the previous bug of forgetting to update the index


for count, value in enumerate(values):
    print(count, value)
