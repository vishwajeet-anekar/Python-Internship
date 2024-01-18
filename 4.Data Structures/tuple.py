# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  
print(my_tuple[-1])  

# Counting occurrences of an element
count = my_tuple.count(3)
print(count)  

# Finding the index of an element
index = my_tuple.index(4)
print(index)  # Output: 3

# Concatenating tuples
other_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + other_tuple
print(concatenated_tuple)  
# Slicing a tuple
slice = my_tuple[1:4]
print(slice)  

# Converting a tuple to a list
my_list = list(my_tuple)
print(my_list)  

# Converting a list to a tuple
new_tuple = tuple(my_list)
print(new_tuple)  