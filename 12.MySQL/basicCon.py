import mysql.connector

def connect():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "roodt",
        database = "vishwajeet"
    )
if __name__ =="__main__":
    # con = connect()
    # if con:
    #     print("connection successful")
    # else: 
    #     print("error")
    try:
        con = connect()
        print('yo')
    except mysql.connector.Error as e:
        print(f"error: {e}")