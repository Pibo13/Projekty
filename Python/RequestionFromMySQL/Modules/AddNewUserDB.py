import mysql.connector

connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
db = 'polpiotech', auth_plugin='mysql_native_password')



id = int(input('Enter ID (It can be left blank): '))
login = str(input('Enter login for new user: '))
password = str(input('Enter password for new user: '))
name = str(input('Enter user name: '))
lastname = str(input('Enter user surname: '))
email = str(input('Enter user adress e-mail: '))


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

print('Added new user', cursor.rowcount, 'to the data base.')

connection.commit()
cursor.close()
connection.close()