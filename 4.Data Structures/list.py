# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Modifying elements
my_list[2] = 6
print(my_list)  # Output: [1, 2, 6, 4, 5]

# Appending elements
my_list.append(7)
print(my_list)  # Output: [1, 2, 6, 4, 5, 7]

# Inserting elements
# my_list.insert(1,'vishu')
# print(my_list)  # output: [1, 'vishu', 2, 6, 4, 5, 7]

# Removing elements
my_list.remove(4)
print(my_list)  # Output: [1, 2, 6, 5, 7]

# Sorting elements
my_list.sort()
print(my_list)  # Output: [1, 2, 5, 6, 7]

# Reversing elements
my_list.reverse()
print(my_list)  # Output: [7, 6, 5, 2, 1]

# Extending the list
my_list.extend([8, 9, 10])
print(my_list)  # Output: [7, 6, 5, 2, 1, 8, 9, 10]

# Counting elements
count = my_list.count(5)
print(count)  # Output: 1

# Slicing the list
slice = my_list[2:5]
print(slice)  # Output: [5, 2, 1]

# Clearing the list
my_list.clear()
print(my_list)  # Output: []

# Deleting the list
del(my_list)
print(my_list)