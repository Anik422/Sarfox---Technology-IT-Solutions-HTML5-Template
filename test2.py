from email.mime.text import MIMEText
import smtplib

# msg = MIMEText("Hello There!")

# msg['Subject'] = 'A Test Message'
# msg['From'] = 'username@gmail.com'
# msg['To'] = 'username@gmail.com'

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()  ##Must start TLS session to port 587 on the gmail server
s.login('fazlumiah2525@gmail.com', 'imranhasan123') ##Must pass args gmail username & password in quotes to authenticate on gmail
# s.sendmail('username@gmail.com',['username@gmail.com'],msg.as_string())

print("Message Sent")