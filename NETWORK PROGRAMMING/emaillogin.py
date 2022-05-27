import smtplib
from email.mime.text import MIMEText
content='this is my text email sent to you by my python program'

msg=MIMEText(content)
fromaddress="iamsender1@gmail.com"
toaddress="iamreciever1@gmail.com"

msg['From']=fromaddress
msg['To']=toaddress
msg['Subject']=" Email throgh python program"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddress,"mypassword")

server.send_message(msg)
print("email sent.")
server.quit()
