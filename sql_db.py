import sqlite3


db = 'records_db.sqlite'


def main():
    # calling functions in the order they should execute
    menu()
    drop_table()
    create_table()
    data()

def menu():
    # Creating a super simple menu
    choice = input('\nPlease choose one of the following here \n 1 to add \n 2 to delete\n 3 to show all \n 4 to update \nAny other key to exit: ')

    if choice == '1':
        create_new_record()
    elif choice == '2':
        delete_record()
    elif choice == '3':
        display_data()
    elif choice == '4':
        update_record()
    else:
        SystemExit()


def drop_table():
    # Clearing the table so ots clean
    with sqlite3.connect(db) as conn:  
        conn.execute('DROP table if exists records')
    conn.close()

def update_record():
    # Getting the info for updating the records records
    name = input('Please enter the record name you wish to update')
    catches = int(input('Please enter the new number of catches'))

    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE records SET catches = ? WHERE name = ?', (catches, name))
    conn.close()
    menu()


def create_table():
    # creating a anew table with 3 columns
    with sqlite3.connect(db) as conn:  
        conn.execute('create table if not exists records (name text, country text, catches int)')
    conn.close()


def data():
    # Inserting some data to work with
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO records values ("James", "Finland", 98)')  # add products
        conn.execute('INSERT INTO records values ("Ian", "Canada", 99)')
        conn.execute('INSERT INTO records values ("Aaron", "Canada", 98)')
        conn.execute('INSERT INTO records values ("Chad", "USA", 99)')
    conn.close()



def display_data():
    # Displaying all the data in the table currently
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records')
    print('All Records: ')
    for row in results:
        print(row)  

    conn.close()
    menu()


def create_new_record():
    # Getting the data to make a brand new record
    name = input('Please enter the new name for the record: ')
    country = input('Please enter their country: ')
    catches = int(input('Please enter the number of catches: '))
    
    # Inserting them into the database with an INSERT statement
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO records VALUES(?, ?, ?)', (name, country, catches))
    conn.close()

    menu()


def delete_record():
    # Getting the name of the record to delete
    delete_name = input('Please enter the name')
    # Deleting from the database with the DELETE statement
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from records WHERE name = ?' , (delete_name,))
    conn.close()
    menu()


main()