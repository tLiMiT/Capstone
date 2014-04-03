# Message Sender

import smtplib

# Stub email account info
email = 'nucapstonec6@gmail.com'
pswd = 'projectC6'
number = '5082210266'

# TODO - add exception handlers
def sendMessage(destination, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,pswd)
    server.sendmail(email, destination, message)

