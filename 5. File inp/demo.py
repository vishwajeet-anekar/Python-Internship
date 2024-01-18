import csv


def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")


def write_text_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Content written to file '{file_path}'.")
    except IOError:
        print(f"Error writing to file '{file_path}'.")


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


# Example usage
text_file_path = 'example.txt'
csv_file_path = 'example.csv'

# Read from text file
text_content = read_text_file(text_file_path)
if text_content:
    print(f"Text file content:\n{text_content}")

# Write to text file
new_text_content = "This is some new content."
write_text_file(text_file_path, new_text_content)

# Read from CSV file
csv_data = read_csv_file(csv_file_path)
if csv_data:
    print(f"CSV file data:")
    for row in csv_data:
        print(row)

# Write to CSV file
new_csv_data = [['Name', 'Age'], ['John', '25'], ['Lisa', '30'], ['Mark', '40']]
write_csv_file(csv_file_path, new_csv_data)