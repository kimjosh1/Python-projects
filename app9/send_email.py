from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="joshuakim4@yahoo.ca"
    from_password="Io500ntgs"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> of people. <br> Thanks!" % (height, average_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    yahoo=smtplib.SMTP('smtp.mail.yahoo.ca', 465)
    yahoo.ehlo()
    yahoo.starttls()
    yahoo.login(from_email, from_password)
    yahoo.send_message(msg)
