# BIBLIOTEKA
import requests


# GET - WYŚWIETLENIE
response = requests.get('https://jsonplaceholder.typicode.com/posts/10')

# SPRAWDZENIE PRAWIDŁOWOŚCI ZAPYTANIA:
if (response.status_code != requests.codes.ok): # STATUS KODU KOMUNIKACJI KLIENT-SERWER.
    print('Coś poszło nie tak...')
else:
    print(response.json()) # WYDRUKOWANIE ZA POMOCĄ FORMATU PLIKU JSON.




# JSON
requestBody = {
    'title' : 'NASZ TYTUŁ',
    'body' : 'TREŚĆ POSTA',
    'userId' : 1
}

# POST - STWORZENIE
response = requests.post('https://jsonplaceholder.typicode.com/posts', json = requestBody)

if (response.status_code != requests.codes.created):
    print('Coś poszło nie tak...')
else:
    print(response.json())
