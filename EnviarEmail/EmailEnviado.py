import email.message
import smtplib


def enviarEmail():
    corpoEmail = """
    <p> Teste </P>

    """
    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['From'] = 'menezes.william.sm@gmail.com'
    msg['To'] = 'menezes.william.sm@gmail.com'
    password = 'jlkogvydwxpyqlmd'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpoEmail)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("Email enviado")


enviarEmail()