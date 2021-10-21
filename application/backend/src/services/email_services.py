# Importación de librerías
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
from src.services.email_messages import MessageFor

class Email():

    def send_email(self: object, message: str, subject: str, email: str) -> None:
        """
        Método enviar email.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             message: str => Mensaje que se enviará en el cuerpo del correo, se requiere HTMl.
                             subject: str => Asunto del correo.
                             email: str => Dirección de correo electrónico a donde llegará el correo.
            |- Retorno -> None;
            |- Función -> Envia un correo desde el email siigobugfinder@outlook.com con el mensaje, asunto y correo entregados
                          por parámetros.
        """
        siigo_email = getenv("EMAIL_ACCOUNT")
        msg = MIMEMultipart()
        msg['From'] = siigo_email
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'html'))

        mailServer = smtplib.SMTP('smtp.live.com',587)
        mailServer.starttls()
        mailServer.login(siigo_email, getenv("EMAIL_PASSWORD"))

        mailServer.sendmail(siigo_email, email, msg.as_string())
        mailServer.close()

    def confirmation_email(self: object, email: str, nickname: str, auth_token: str):
        """
        Método email de confirmación.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             email: str => Dirección de correo electrónico a donde llegará el correo.
                             nickname: str => Nickname con el que se identifica el jugador.
                             auth_token: str => Token que contiene la informacion del jugador.
            |- Retorno -> None;
            |- Función -> Envia un correo desde el email siigobugfinder@outlook.com con el mensaje, asunto y correo entregados
                          por parámetros.
        """
        message: str = MessageFor.confirmation_email(nickname, auth_token)
        subject = "Please confirm your email"
        self.send_email(message, subject, email)
