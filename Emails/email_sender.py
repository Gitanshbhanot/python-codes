import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Gitansh Bhanot'
email['to'] = 'gitanshbhanot86@gmail.com'
email['subject'] = 'You Won 1,000,000 dollars'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print('all good boss!')
