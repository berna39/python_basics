class Incrementer:
    def __iter__(self):
        self.i = 0
        return self.i
    def __next__(self):
        self.i += 1
        return self.i

inc = Incrementer()
print(next(inc))
