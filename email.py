import smtplib
from mailconstants import *
from email.mime.text import MIMEText

def sendMail():
    try:
        name = username
        passw = password

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(name, passw)
        msg = "Hello! Welcome"
        server.sendmail(name, name, msg)
        server.close()
        print("mail sent successfuly")
    except Exception as e:
        print("Failed to send mail:",e)


def sendmailsubject():
    msg = MIMEText("Hello!! Send mail with Subject")

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Here goes subject'
    msg['From'] = username
    msg['To'] = username

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp.gmail.com:587')
    print("Sending mail")
    s.ehlo()
    s.starttls()
    s.login(username, password)
    s.sendmail(username, username, msg.as_string())
    print("Mail sent")
    s.quit()

sendmailsubject()
sendMail()
