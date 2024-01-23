from conn import database
from crud import crudfunc as funct

def main():
    db_host = "localhost"
    db_user = "root"
    db_password = "root"
    db_name = "vishwajeet"

    db = database(db_host, db_user, db_password, db_name)
    app = funct(db)

    while True:
        print("\n1 . Create Record")
        print("2. Read Records")
        print("3. Update Records")
        print("4. Delete Record")
        print("5. Complex Query")
        print("6. Exit")

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter Your Name : ')
            email = input('Enter your Email: ')
            app.create_record(name, email)
        elif choice == '2':
            app.read_record()
        elif choice == '3':
            user_id = int(input('Enter ID you want to Update: '))
            new_name = input('Enter the new Name: ')
            new_email = input('Enter the new Email: ')
            app.update_record(user_id, new_name, new_email)
        elif choice == '4':
            user_id = int(input('Enter id to Delete: '))
            app.delete_record(user_id)
        elif choice == '5':
            app.complex_query()
        elif choice == '6':
            break
        else:
            print('Enter the Valid Choice')

    db.close()

if __name__ == "__main__":
    main()