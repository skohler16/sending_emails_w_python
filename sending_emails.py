import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From'] = "Scooter"
email['To'] = 'skohler16@gmail.com'
email['Subject'] = 'This is NOT a test and you just won a ton!!'

# email.set_content(html.substitute(name='TinTin'))

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as connection:
    connection.ehlo()
    email_address = 'sdaicmd@gmail.com'
    email_password = 'muvi xmga ubmf pqto'
    connection.login(email_address, email_password )
    connection.sendmail(from_addr=email_address, to_addrs='skohler16@gmail.com',
    msg = html.substitute(name = 'TinTin'))
    print('all good boss!')