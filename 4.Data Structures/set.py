# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set) 

# Discarding elements
# the remove() method will raise an error if the specified item does not exist, and the discard() method will not
my_set.discard(3)
print(my_set)

# Removing elements
my_set.remove(3)
print(my_set) 

# Checking if an element exists
if 2 in my_set:
    print("2 exists in the set")

# Checking the length of the set
length = len(my_set)
print(length) 

# Union of sets
other_set = {4, 5, 6, 7, 8}
union_set = my_set.union(other_set)
print(union_set)  

# Intersection of sets
intersection_set = my_set.intersection(other_set)
print(intersection_set) 

# Difference of sets
difference_set = my_set.difference(other_set)
print(difference_set)  

# Subset check
subset = {1, 2}
print(subset.issubset(my_set))  

# Superset check
superset = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(superset.issuperset(my_set))  

# Clearing the set
my_set.clear()
print(my_set)  