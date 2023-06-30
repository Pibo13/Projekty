import tkinter as tk
from PIL import GifImagePlugin, ImageTk
from dotenv import load_dotenv
from os import getenv, system, times_result
import getpass
import os
import sys
import time


login = str ("polpiotech") 
#login2 = ('piotrek')
haslo = str ("123")
#haslo2 = str ('321')
password = haslo


winlog = os.getlogin()

import os
print('-- Panel logowania --')
print()
print()
data0 = int (input('DATA: '))
godz0 = int (input('GODZINA: '))
data1 = str (data0)
godz1 = str (godz0)
print()
login = getpass.getpass("LOGIN: ")
password = getpass.getpass("HASŁO: ")
id = input("TWOJE ID: ")
print()
print()
os.system("cls")

idUN = id
timeNow = time.asctime()
nazwaPliku = 'ID-' + idUN + '-D-'+ data1 + '-H-' + godz1 + '.txt'

while True:
    if login == str ("polpiotech") and haslo == str ("123"):
        os.system("cls") 
        ekran = sys.stdout
        sys.stdout = open(nazwaPliku, 'w') 
        print('INFORMACJE O LOGOWANIU:')
        print()
        load_dotenv()
        print(timeNow)
        
        print()
        print('E-MAIL:', getenv('USERNAME1'))
        print("ID UŻYTKOWNIKA: " f"{id}", '-', getenv(idUN))
        print('LOGIN WIN:', winlog)
        print()
        sys.stdout=ekran
        os.system('move *.txt D:\\PYTHON\\E-Mail\\infoLog\\')
        os.system('cls')
        print(timeNow)
        print()
        print('E-MAIL:', getenv('USERNAME1'))
        print("ID UŻYTKOWNIKA: " f"{id}", '-', getenv(idUN))
        print('LOGIN WIN:', winlog)
        print()        
        print()        
        print()

        
        
        root = tk.Tk() 
        root.geometry('400x600') 
        root.title('POLPIOTECH®')

        class App:
            if __name__ == '__main__':

                glowneMenu = tk.Menu()
                root.config(menu = glowneMenu)

                fileMenu = tk.Menu(glowneMenu) 
                glowneMenu.add_cascade(label='Połącz', menu = fileMenu)
                podMenu = tk.Menu(fileMenu) 
                fileMenu.add_cascade(label='Użytkownik', menu = podMenu) 
                podMenu.add_command(label = 'Zarejestruj konto') 
                podMenu.add_command(label = 'Reset hasła')
                podMenu.add_command(label = 'Anuluj')
                fileMenu.add_command(label = 'Wyloguj')
                fileMenu.add_separator() 
                fileMenu.add_command(label = 'Zamknij')
                

                l0 = tk.Label(root, text = 'POLPIOTECH®')
                l0.pack()
                
                l1 = tk.Label(root, text = 'Piotr Kazimierz Bodych')
                l1.pack(side=tk.BOTTOM) 

                zdjecie1 = GifImagePlugin.GifImageFile('polish-flag-23.gif')
                GifImagePlugin.RAWMODE
                ikona1 = ImageTk.PhotoImage(zdjecie1)
                tk.Label(root, image=ikona1).pack()

                l2 = tk.Label(root, text = 'Program do wysyłania wiadomości e-main' '\n' ' w sposób z automatyzowany za pomocą szablonu wiadomości HTML.')
                l2.pack()



                def funPrzypisana0():
                    print('-- WYWOŁANIE PROCESU --')
                    print()
                    print()
                    print('-- Uruchomiono modół główny [MAIN]...')
                    t = 0
                    while t < 8:
                        t = t + 1
                        time.sleep(1)
                        break
                    print(f"ŁADOWANIE MODUŁU: {t}", "s.")
                    print()
                    print()
                    import main
                    print('-- Logowanie na serwer SMTP [POST-ADAPTER]...')
                    while True:
                        t < 12
                        t = t + 1
                        time.sleep(1)
                        break
                    print(f"ŁADOWANIE MODUŁU: {t}", "s.")
                    print()
                    print()
                    print('-- Ładowanie szablonu HTML [MESSAGES]...')
                    print()
                    print()
                    print('-- Rozpoczęcie procesu adresaci wiadomości e-mail [MAIN]...')
                    print('   -- Importowanie adresu e-mail odbiorcy wiadomości...')
                    print('      -- Ustawianie tematu wiadomości e-mail...')
                    print()
                    print()
                    print('-- Zlecono wysłanie wiadomości e-mail...')
                    print('  --> PROCES OK! <--')
                    print()
                    

                    

                b0 = tk.Button(root, text = 'WYŚLIJ E-MAIL', command=funPrzypisana0, width=16, bg='white', fg='red')
                b0.place(x=66, y=473)

                def funPrzypisana1(event):
                    print('-- Zamykanie aplikacji...')
                    os.system('App.bat')

                b1 = tk.Button(root, text = 'ZAMKNIJ', command=funPrzypisana1, width=16, bg='red', fg='white') 
                b1.bind('<Button-1>', funPrzypisana1)
                b1.pack()
                b1.place(x=202, y=473)

                root.mainloop()
    else:
        print("BŁĘDNE POŚWIADCZENIA!")
        break

