import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Scooter"
email['to'] = 'skohler16@gmail.com'
email['subject'] = 'This is a test and only a test'

email.set_content('He is a python master')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as connection:
    email_address = 'sdaicmd@gmail.com'
    email_password = 'muvi xmga ubmf pqto'
    connection.login(email_address, email_password )
    connection.sendmail(from_addr=email_address, to_addrs='skohler16@gmail.com',
    msg="subject:hi \n\n this is my message")
    print('all good boss!')