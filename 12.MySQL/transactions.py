# If both execute statements are successful, the transaction is committed using conn.commit(). If an error occurs during the execution of the SQL statements, the transaction is rolled back using conn.rollback().
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "vishwajeet"
)
cursor = conn.cursor()# Cursor object created

try:
    conn.start_transaction()
    cursor.execute("insert into users (name, email) values ('demo', 'dmeo@123')")
    cursor.execute("insert into users (names, email) values ('demo1', 'dmeo1@123')")
    conn.commit()
    print('transaction committed')
except mysql.connector.Error as e:
    conn.rollback()
    print(f'error: {e}')
finally :
    cursor.close()
    conn.close()
