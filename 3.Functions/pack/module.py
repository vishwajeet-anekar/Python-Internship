#this file is a single module that contains all the functions
from functools import reduce

#*args accepts multiple agruments in sets
def find_sum(*args):
    return sum(args)

#**kwargs accepts multiple arguments in dictionary
def concatenate_strings(**kwargs):
    return ' '.join(kwargs.values())

#lambda function is used to create an anonymous function
# map is used to apply a function to all items in a list, takes function, list as arguments
def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

#reduce is used to apply a function to all items in a list, takes function, list as arguments
# basically it iterates through list one by one and applies the function
def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)


#filter filters a sequence based on a function and return a boolean value
# filter accepts a function and a list 
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

#recursive function - function that calls itself
def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number - 1)