import csv
import os

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")


def write_csv_file(file_path, data):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            print(f"Data written to CSV file '{file_path}'.")
    except IOError:
        print(f"Error writing to CSV file '{file_path}'.")


def append_csv_file(file_path, data):
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            print(f"Data appended to CSV file '{file_path}'.")
    except IOError:
        print(f"Error appending to CSV file '{file_path}'.")


def update_csv_file(file_path, row_index, column_index, new_value):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]

        if row_index < len(rows) and column_index < len(rows[row_index]):
            rows[row_index][column_index] = new_value

            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                print(f"CSV file '{file_path}' updated.")
        else:
            print(f"Invalid row or column index in CSV file '{file_path}'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error updating CSV file '{file_path}'.")


def delete_csv_file(file_path):
    try:
        os.remove(file_path)
        print(f"CSV file '{file_path}' deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error deleting CSV file '{file_path}'.")


# Example usage
csv_file_path = 'example.csv'

# Read from CSV file
csv_data = read_csv_file(csv_file_path)
if csv_data:
    print(f"CSV file data:")
    for row in csv_data:
        print(row)

# Write to CSV file
new_csv_data = [['Name', 'Age'], ['John', '25'], ['Lisa', '30'], ['Mark', '40']]
write_csv_file(csv_file_path, new_csv_data)

# Append to CSV file
additional_csv_data = [['Sarah', '35'], ['Michael', '45']]
append_csv_file(csv_file_path, additional_csv_data)

# Update CSV file
update_csv_file(csv_file_path, 1, 1, '26')

# Delete CSV file
# delete_csv_file(csv_file_path)