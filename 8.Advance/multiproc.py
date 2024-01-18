import multiprocessing

# Function to be executed by each process
def calculate_sum(numbers):
    total = sum(numbers)
    return total

# Main program
if __name__ == "__main__":
    # Create a list of numbers
    numbers = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    # Create a process pool with 2 processes
    pool = multiprocessing.Pool(processes=2)

    # Apply the calculate_sum function to each sub-list in parallel
    results = pool.map(calculate_sum, numbers)

    # Close the pool
    pool.close()

    # Print the results
    print(results)