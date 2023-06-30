import requests
import json

ingredients = input('Podaj składniki: ')
queryString = input('Co chcesz wyszukać: ')

response = requests.get(f'http://www.recipepuppy.com/api/?i={ingredients}&q={queryString}')

if (response.status_code != requests.codes.ok):
    print('Coś poszło nie tak...')
else:
    print(json.dumps(response.json(), indent=4))