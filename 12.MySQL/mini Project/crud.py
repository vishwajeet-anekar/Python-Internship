class crudfunc:
    def __init__(self,database):
        self.database = database
    
    def create_record(self,name,email):
        query = "insert into users (name, email) values (%s,%s)"
        data = (name,email)
        self.database.exec(query,data)# database object exec execute query
        self.database.commit()
        print("Record inserted successfully.......")
        
        
    def read_record(self):
        query = "select * from users"
        records = self.database.exec(query,fetch_all = True)
        if not records:
            print('No records found')
        else:
            for i in records:
                print(f'ID:{i[0]}, Name:{i[1]}, Email:{i[2]}')
        
        
    def update_record(self,user_id,new_name,new_email):
        query = "update users set name = %s, email = %s where id = %s"
        data = (new_name,new_email,user_id)
        self.database.exec(query,data)
        self.database.commit()
        print("records inserted successfully")

        
    def delete_record(self,user_id):
        query = "delete from users where id = %s"
        data = (user_id,)
        self.database.exec(query,data)
        self.database.commit()
        print('record deleted successfully')
        
        
    def complex_query(self):
        query = """
        with emaiCTE as (
            select id, name, email, length(email) as email_length 
            from users
        )
        select u.id, u.name, u.email,e.email_length from users u
        join emaiCTE e on u.id = e.id
        order by e.email_length desc
        """
        records = self.database.exec(query,fetch_all = True)
        if not records:
            print('No records found')
        else:
            for i in records:
                print(f'ID:{i[0]}, Name:{i[1]}, Email:{i[2]}, Email Length:{i[3]}')