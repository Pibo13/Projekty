import mysql.connector
import os


connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
db = 'polpiotech', auth_plugin='mysql_native_password')

cursor = connection.cursor()

query = 'SELECT * FROM users'
cursor.execute(query)
for (id, login, password, name, lastname, email) in cursor:
    print('ID - LOGIN - HASŁO - IMIĘ - NAZWISKO - E-MAIL')
    print(f'{id}', '|',f'{login}', '|',f'{password}', '|', f'{name}', '|', f'{lastname}', '|', f'{email}')
    print('--'*40)

connection.commit()
cursor.close()
connection.close()

os.system('python ShowAllUsers.py >F:\\PYTHON\\RequestionFromMySQL\\db_MySQL-UsersLog.txt')
