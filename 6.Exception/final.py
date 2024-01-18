# User-defined exception
class NegativeNumberException(Exception):
    pass

# Function that performs division
def divide_numbers(a, b):
    try:
        if b < 0:
            raise NegativeNumberException("Second number cannot be negative")
        result = a / b
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Error: Division by zero")
    except NegativeNumberException as e:
        print("Error:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("Division operation completed")

# Main program
try:
    # Prompt the user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform division
    divide_numbers(num1, num2)

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

except Exception as e:
    print("An error occurred:", str(e))