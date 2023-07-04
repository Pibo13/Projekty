import mysql.connector
import os
import sys

def menu():
    print('   -- OPERATION IN DATA BASE MYSQL --')
    print('--'*20)
    print('[1] -- show all users.')
    print('[2] -- add new user.')
    print('[3] -- change user password.')
    print('[4] -- delete user of data base.')
    print('[0] -- exit program')
    print()
    
    choiceOption = int(input('CHOSSE OPTIONS: '))
    return(choiceOption)

driver = 1
while driver != 0:
    driver=menu()

    if driver == 1:
        os.system('cls')
        print('Option showing all account users.')
        print('--'*20)

        connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
        db = 'polpiotech', auth_plugin='mysql_native_password')

        cursor = connection.cursor()

        query = 'SELECT * FROM users'
        cursor.execute(query)
        for (id, login, password, name, lastname, email) in cursor:
            print('ID - LOGIN - HASŁO - IMIĘ - NAZWISKO - E-MAIL')
            print(f'{id}', '|',f'{login}', '|',f'{password}', '|', f'{name}', '|', f'{lastname}', '|', f'{email}')
            print('--'*40)
            print()
        connection.commit()
        cursor.close()
        connection.close()

        os.system('pause')
        os.system('cls')
    
    elif driver == 2:
        
            os.system('cls')
            print('It is option add new user.')
            print('--'*20)
            connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
            db = 'polpiotech', auth_plugin='mysql_native_password')

            try:
                id = int(input('Enter ID: '))
                login = str(input('Enter login for new user: '))
                password = str(input('Enter password for new user: '))
                name = str(input('Enter user name: '))
                lastname = str(input('Enter user surname: '))
                email = str(input('Enter user adress e-mail: '))
            except ValueError:
                while True:
                    if id != int:
                        print()
                        print('Mistake: ID must be number!')
                        os.system('pause')
                        os.system('cls')
                        print('Information: Sorry, but the program needs to be closed, because it has to start working again.')
                        print()
                        print()
                        print('If you want try running again the program and perform operations.')
                        print('You must remember that ID must have values integer numbers.')
                        os.system('pause')
                        sys.exit(0)
                        
                    else: 
                        continue

            cursor = connection.cursor()
            insertQuery = "INSERT INTO users(id, login, password, name, lastname, email) VALUES(%(id)s, %(login)s, %(password)s, %(name)s, %(lastname)s, %(email)s)"

            insertData = {
                'id' : f'{id}',
                'login' : f'{login}',
                'password' : f'{password}',
                'name' : f'{name}',
                'lastname' : f'{lastname}',
                'email' : f'{email}',
            }
            cursor.execute(insertQuery, insertData)
            print()
            print('Added', cursor.rowcount, 'new user to the data base.')

            connection.commit()
            cursor.close()
            connection.close()

            os.system('pause')
            os.system('cls')


    elif driver == 3:
        os.system('cls')
        print('This option do make change password in user account.')
        print('--'*20)
        connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
        db = 'polpiotech', auth_plugin='mysql_native_password')

        cursor = connection.cursor()

        id_user = str(input('Enter user ID: '))
        password_user = str(input('Enter new user password: '))

        query = 'UPDATE users SET users.password='f'{password_user} WHERE users.id='f'{id_user}'
        cursor.execute(query)
        print()
        print('Changed user password in', cursor.rowcount, 'row of data.')

        connection.commit()
        cursor.close()
        connection.close()

        os.system('pause')
        os.system('cls')

    elif driver == 4:
        os.system('cls')
        print('Option delete user account of data base.')
        print('--'*20)

        connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
        db = 'polpiotech', auth_plugin='mysql_native_password')

        id_user = input('Enter user ID: ')
        cursor = connection.cursor()
        query = 'DELETE FROM users WHERE users.id='f'{id_user}'

        cursor.execute(query)
        print()
        print('Deleted', cursor.rowcount, 'row(s) of data.')

        connection.commit()
        cursor.close()
        connection.close()

        os.system('pause')
        os.system('cls')