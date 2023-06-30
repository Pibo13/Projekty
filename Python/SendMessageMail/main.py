from post_adapter import PostAdapter

from messages import WelcomeMessage

from dotenv import load_dotenv
from os import getenv
import tkinter

load_dotenv()

mailer = PostAdapter(
    host='smtp.poczta.onet.pl', 
    port=465, 
    username=getenv('USERNAME1'), 
    password=getenv('PASSWORD') 
)

mailer.login()

welcome = WelcomeMessage()

mailer.send_mail(
    recipient_email = 'p.bodych1993@outlook.com', 
    subject = 'Nazwywam się PREDATOR.', 
    content = welcome.render(name='POLPIOTECH®'))