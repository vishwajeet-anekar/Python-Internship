import re 
def validate_login(email, password):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    password_pattern = r'^[a-zA-Z0-9_-]{6,20}$'

    if re.match(email_pattern, email) and re.match(password_pattern, password):
        return True
    else:
        return False

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if validate_login(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()