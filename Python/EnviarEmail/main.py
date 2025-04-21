import smtplib
from email.mime.text import MIMEText

def enviar_correo(destinatario, asunto, mensaje):
    remitente = 'tu_correo@example.com'
    password = 'tu_contraseña'
    msg = MIMEText(mensaje)
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario

    with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(remitente, password)
            server.sendmail(remitente, destinatario, msg.as_string())

enviar_correo('destinatario@example.com', 'Asunto del correo', 'Mensaje del correo')