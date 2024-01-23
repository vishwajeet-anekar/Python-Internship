import mysql.connector 

class database:
    def __init__(self,host,user,password,database_name):
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database_name
        )
        self.create_table()
    
    def create_table(self):
        create_query = """ 
        create table if not exists users(
            id int auto_increment primary key,
            name varchar(20)not null,
            email varchar(20) not null
        )
        """
        with self.connection.cursor() as cursor:
            cursor.execute(create_query)
            
    def exec(self,query,data = None, fetch_all = None):
        with self.connection.cursor() as cursor:
            cursor.execute(query,data)
            if fetch_all:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
            
    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()