import logging

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def login(username, password):
    if username == "admin" and password == "password":
        logging.info(f"User {username} logged in successfully.")
        return True
    else:
        logging.warning(f"Failed login attempt for user {username}.")
        # logging.error(f"Invalid credentials for user - error{username}.")
        # logging.critical(f"this is the critical error for user - critical{username}.")
        return False

login("admin", "password")
login("vishwajeet", "123456")