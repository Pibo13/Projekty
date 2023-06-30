import random
import os
import time
import pathlib


chain = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLŁMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+'
long_password = int(input('Ilość znaków: '))

password = ''.join(random.sample(chain, long_password))
print('--'*25)
#print('Przykładowe hasło ' f'{long_password} znakowe')
print('Wygenerowane hasło:', password)
print('--'*25)

fileName = str(input('Nazwa pliku: '))
text = str(input('Aplikacja / System: '))
with open(fileName + '.txt', 'w') as f:
    f.write('Wygenerowane hasło: ' f'{password} \n {text}')