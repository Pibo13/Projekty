# -- IMPORTOWANIE BIBLIOTEKI WYMAGANEJ DO DZIAŁANIA KODU Z SERVEREM POCZTY WYCHODZĄCEJ (smtp)
import smtplib

# -- WYSYŁANIE WIADOMOŚCI E-MAIL W FORMACIE HTML. (import funkcji wymagany do budowy mechanizmu wysyłania wiadomości)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# PRZEKAZANIE WARTOŚĆ ZMIENNYCH (username / password) DO ZMIENNYCH (self.)
# ORAZ NAWIĄZANIE POŁĄCZENIA Z SERVEREM SMPT DOMENY POCZTY E-MAIL (host / port).
class PostAdapter:
    def __init__(self, host: str, port: int, username: str, password: str): # --SUPER METODA - PRZUPISANIE ZMIENNYCH.
        self.username = username # --KONWERSJA / PRZYPISANIE ZMIENNYCH DO METODY.
        self.password = password # -- KONWERSJA / PRZYPISANIE ZMIENNYCH DO METODY.
        self.server = smtplib.SMTP_SSL(host, port) # -- PRZYPISANIE DO "METODO-ZMIENNEJ" OPCJI (konstruktor???) 
        # -- NAWIĄZANIA KOMUNIKACJI Z SERVEREM SMTP I ZADEKLAROWANIE ZMIENNYCH (host / port).

# LOGOWANIE NA SERVER SMTP POCZTY E-MAIL.
    def login(self):
        self.server.ehlo() # -- NAWIĄZANIE POŁĄCZENIA Z SERVEREM POCZTOWY.
        self.server.login(self.username, self.password) # -- LOGOWANIE DO KONTA E-MAIL.

# -- DANE ZAMIESZCZONE W TREŚCI WIADOMOŚCI (recipient_emial: ADRES E-MAIL ODBIORCY, 
# -- subject: TEMAT WIADOMOŚCI, content: TREŚĆ WIADOMOŚCI).
    def send_mail(self, recipient_email: str, subject: str, content: str):
        message = self._compose_message(content, recipient_email, subject) # -- KONWERSJA ZMIENNYCH DO ZMIENNYCH W METODZIE (self.)
        self.server.sendmail(self.username, recipient_email, message.as_string()) # -- WYSŁANIE WIADOMOŚCI E-MAIL.

#KOMPONOWANIE WIADOMOŚCI E-MAIL (zewnętrzna metoda).        
    def _compose_message(self, content, recipient_email, subject): # -- _nazwa_metody_: ZNAK PRZED I PO "_" OZNACZA, ŻE NAZWA METODY JEST PRYWATNA.   
        message = MIMEMultipart('alternative') # -- METODA DZIĘKI, KTÓREJ TWORZYMY WIADOMOŚĆ E-MAIL.
        message['Subject'] = subject # -- PRZYPISANIE W WIADOMOŚCI TREŚCI TEMAT.
        message['From'] = self.username # -- PRZYPISANIE W WIADOMOŚCI TREŚCI NADAWCY.
        message['To'] = recipient_email # -- PRZYPISANIE W WIADOMOŚCI TREŚCI ODBIORCY.
        message.attach(
            MIMEText(content, 'html') # -- WIADOMOŚĆ DO WYSŁANIA W FORMACIE (html).
            )

        return message # ZWRÓCENIE ZMIENNEJ ODPOWIADAJĄCEJ ZA KONSTRUKCJE OBIEKTU WIADOMOŚĆ.
    
    def __del__(self):
        self.server.close()