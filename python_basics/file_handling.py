# readline allows us to read only one line
t = open("testing.txt", "rt").readline()
print(t)

#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
u = open('testing.txt', 'rt').read()
print(u)

#writing
with open('my_first_file.txt', 'w') as f:
    f.write('The lord of the ring')



