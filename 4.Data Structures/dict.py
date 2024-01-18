# Creating a dictionary
my_dict = {"name": "Vishwajeet",
           "age": 22,
           "city": "Pune"}

# Accessing values
print(my_dict["name"]) 
print(my_dict.get("age"))  

# Modifying values
my_dict["age"] = 100
print(my_dict) 

# Adding new key-value pairs
my_dict["occupation"] = "DATA QA"
print(my_dict)  

# Removing key-value pairs
del my_dict["city"]
print(my_dict)  

# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary")

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()
print(keys)  
print(values)  

# copy the dictionary
new_dict = my_dict.copy()
print(new_dict)

# Clearing the dictionary
my_dict.clear()
print(my_dict)  