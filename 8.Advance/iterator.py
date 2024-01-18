class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Create an instance of the iterator
my_iterator = MyIterator(1, 5)

# Iterate over the elements using a for loop
for element in my_iterator:
    print(element)

# Create another instance of the iterator
my_iterator2 = MyIterator(10, 15)

# Manually iterate over the elements using the next() function
while True:
    try:
        element = next(my_iterator2)
        print(element)
    except StopIteration:
        break