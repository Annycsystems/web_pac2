from cryptography.fernet import Fernet
import secrets
import string
import smtplib

OTP = ''
digit = string.digits

for i in range(6):
    OTP += str(''.join(secrets.choice(digit)))

message = OTP
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print(OTP)
decMessage = fernet.decrypt(encMessage).decode()

mail_user = 'jose.chavero@cgconsultoresjuridicos.mx'
mail_password = 'HKo2vgYLXgQt'

sent_from = mail_user
to = 'josechaveroo@outlook.es'
subject = 'Important Message MX_Token_CJ 19/09/2022'
body = "Buenos dias\n\nclave token:"

email_text = """\
From: %s
To: %s
Subject: %s

%s
%s
""" % (sent_from, to, subject, body, OTP)

try:
    server = smtplib.SMTP_SSL('smtp.ipage.com', 465)
    server.ehlo()
#     server.starttls()
    server.login(mail_user, mail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

user = input("Ingrese token recibido:")
encMessage2 = fernet.encrypt(user.encode())
print("original string: ", user)
print("encrypted string: ", encMessage2)
decMessage2 = fernet.decrypt(encMessage2).decode()
print(decMessage == decMessage2)
