import os
import smtplib, ssl
from dotenv import load_dotenv

# Laad de variables uit de dotenv omgeving
load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

# Haal het wachtwoord veilig op via de evironment variable
    username = "thom.debets@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")

    receiver = "thom.debets@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email("Hello, how are you?")

