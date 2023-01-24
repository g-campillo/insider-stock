import smtplib
import ssl
from email.message import EmailMessage

class Email:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self._password = password
        self.context = ssl.create_default_context()
    
    def send_mail(self, subject, body, recipients):
        data = EmailMessage()
        data['From'] = self.username
        data['To'] = recipients
        data['Subject'] = subject
        data.set_content(body)
        
        with smtplib.SMTP_SSL(self.host, self.port, context=self.context) as server:
            server.login(self.username, self._password)
            server.sendmail(self.username, recipients, data.as_string())