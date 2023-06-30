# SZABLONY WYSYŁANYCH WIADOMOŚCI E-MAIL.
import jinja2

# ZARZĄDZANIE SZABLONAMI WYSYŁANEJ WIADOMOŚCI E-MAIL - KONSTRUKTOR WYSZUKIWANIA SZABLONU.
class Message:
    def __init__(self):
        template_loader = jinja2.FileSystemLoader(searchpath="./") # NARZĘDZIE SŁUŻĄCE DO ŁADOWANIA SZABLONÓW (szablon wiadomości).
        self.template_env = jinja2.Environment(loader=template_loader) # ŚRODOWISKO: OBIEKT WSPOMAGAJĄCY BUDOWANIE SZABLONU.
        self.template = self.template_env.get_template(self.TEMPLATE_FILE) # ŁADOWANIE SZABLONU.

# METODA DO PRZEKAZYWANIA ARGUMENTÓW.
    def render(self, **kwargs):
        return self.template.render(**kwargs) 


# DZIEDZICZENIE PARAMETRÓW - WYBIERANIE SZABLONU WIADOMOŚCI E-MAIL.
class WelcomeMessage(Message): 
    TEMPLATE_FILE = './templates/cv.html'