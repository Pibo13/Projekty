import mysql.connector



connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
db = 'polpiotech', auth_plugin='mysql_native_password')

print('-- DELETED ROW(S) IN DATA BASE OF MySQL --')
id_user = input('Enter user ID: ')
cursor = connection.cursor()
query = 'DELETE FROM users WHERE users.id='f'{id_user}'

cursor.execute(query)

print('Deleted', cursor.rowcount, 'row(s) of data.')

connection.commit() # POTWIERDZA USUNIĘCIE REKORDU Z BAZY DANYCH.
cursor.close()
connection.close()