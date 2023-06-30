import mysql.connector

connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
db = 'polpiotech', auth_plugin='mysql_native_password')

cursor = connection.cursor()

print('-- CHANGE USER PASSWORD IN DATA BASE OF MySQL --')
id_user = str(input('Enter user ID: '))
password_user = str(input('Enter new user password: '))

query = 'UPDATE users SET users.password='f'{password_user} WHERE users.id='f'{id_user}'
cursor.execute(query)
print('Changed user password in', cursor.rowcount, 'row of data.')

connection.commit()
cursor.close()
connection.close()