# from package pack import module 

from pack import module as m
# from modueles.module import square_numbers as m

def main():
    print("Sum of numbers:", m.find_sum(1, 2, 3, 4, 5))
    print("Concatenated string:", m.concatenate_strings(name="Vishwajeet", age="22", city="Pune"))
    numbers = [1, 2, 3, 4, 5]
    print("Squared numbers:", m.square_numbers(numbers))
    print("Product of numbers:", m.multiply_numbers(numbers))
    print("Even numbers:", m.filter_even_numbers(numbers))
    print("Factorial of 10:", m.fact(5))

if __name__ == "__main__":
    main()