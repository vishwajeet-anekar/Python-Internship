# Example program demonstrating built-in exceptions

# TypeError
try:
    x = 5 + "hello"
except TypeError as e:
    print("TypeError:", str(e))

# ValueError
try:
    int("abc")
except ValueError as e:
    print("ValueError:", str(e))

# ZeroDivisionError
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", str(e))

# IOError
try:
    file = open("nonexistent_file.txt", "r")
except IOError as e:
    print("IOError:", str(e))

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("IndexError:", str(e))

# KeyError
try:
    my_dict = {"name": "John", "age": 25}
    print(my_dict["gender"])
except KeyError as e:
    print("KeyError:", str(e))

# NameError
try:
    print(x)
except NameError as e:
    print("NameError:", str(e))

# FileNotFoundError
try:
    with open("nonexistent_file.txt", "r") as file:
        contents = file.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", str(e))

# SyntaxError
try:
    if True:
        print("Hello")
except SyntaxError as e:
    print("SyntaxError:", str(e))