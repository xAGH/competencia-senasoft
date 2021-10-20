import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email():

    def send_email(self, message, subject, email):

        msg = MIMEMultipart()
        msg['From'] = "siigobugfinder@outlook.com"
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'html'))

        mailServer = smtplib.SMTP('smtp.live.com',587)
        mailServer.starttls()
        mailServer.login("siigobugfinder@outlook.com","senasoft2021")


        mailServer.sendmail("siigobugfinder@outlook.com", email, msg.as_string())
        mailServer.close()

    def confirmation_email(self, email, nickname, auth_token):
        message = f"""<h1>Works {nickname}.\n<a href="http://localhost:4000/users/auth/{auth_token}">Confirm</a></h1>"""
        subject = "Please confirm your email"
        self.send_email(message, subject, email)
