import smtplib

def sendMail():
    try:
        fromuser = "xyz@gmail.com"
        to = "xyz@gmail.com"
        username = "xyz@gmail.com"
        password = "**********"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        msg = "Hello! Welcome"
        server.sendmail(fromuser, to, msg)
        server.close()
        print("mail sent successfuly")
    except Exception as e:
        print("Failed to send mail:",e)

sendMail()



