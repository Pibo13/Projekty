# POŁĄCZENIE DO BAZY DANY MYSQL

import mysql.connector

# POŁĄCZENIA Z BAZĄ DANYCH:
connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',
db = 'polpiotech', auth_plugin='mysql_native_password')

# KONSTRUKTOR OBIEKTU:
cursor = connection.cursor() # OBIEKT DZIĘKI KTÓREMU MOŻEMY WYKONYWAĆ ZAPYTANIA DO BAZY DANYCH.

# TREŚĆ KWERENDY (dodanie nowego użytkownika):
insertQuery = "INSERT INTO users(id, login, password, name, lastname, email) VALUES(%(id)s, %(login)s, %(password)s, %(name)s, %(lastname)s, %(email)s)"

# JSON - (dane użytkownika do zapisu w MySQL):
insertData = {
    'id' : '15',
    'login' : 'kkowara',
    'password' : '191',
    'name' : 'Klaudia',
    'lastname' : 'Kowara',
    'email' : 'klakow@gamil.pl'
}
# WYKONANIE ZAPYTANIA (parametry przekazane do QUERY)
cursor.execute(insertQuery, insertData)

# WYKONANIE COMMITA (możliwość wykonania zapytania w sposób zrozumiały przez MySQL - WYKONANIE PROCESU W MYSQL)
connection.commit()


# TREŚĆ KWERENDY:
query = 'SELECT id, login, password, name, lastname, email FROM users' # KWERENDA MYSQL.
cursor.execute(query) # WYŚWIETLENIE KWERENDY.

# PĘTLA Z PREZENTACJĄ DANYCH Z ZAPYTANIA DO BAZY DANYCH:
for (id, login, password, name, lastname, email) in cursor:
    print('ID - LOGIN - HASŁO - IMIĘ - NAZWISKO - E-MAIL')
    print(f'{id}', '-',f'{login}', '-',f'{password}', '-', f'{name}', '-', f'{lastname}', '-', f'{email}')
    print('-' * 58)

# ZAMKNIĘCIE POŁĄCZENIA Z BAZĄ DANYCH MYSQL:
connection.close()