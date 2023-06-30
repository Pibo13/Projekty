#API in PYTHON library PyStart

# GET - odbieranie (POBIERANIE)
# POST - wysłać
# PUT - ZMIEŃ
# DELET - usuąć

# PROJEKT POBIERANIA KURSU WALUT - API NBP

from urllib import response
import requests

req_get_api = requests.get('https://api.nbp.pl/api/exchangerates/tables/A/') # zmienna zawierająca zapytanie o dane. (TABELA z API NBP)
response = req_get_api.json() # przypisanie wyniku zapytania do zmiennej (format JSON)
print(response[0]['rates'])

for rate in response[0]['rates']:
    print(rate['code'])
    print(rate['mid'])
    print(rate['currency'])
    print('-' * 20)





