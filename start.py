import os
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email():
	os.system('clear')
	login = 'artemrezanov00@mail.ru'
	password = 'awsedrft123'
	url = 'smtp.mail.ru'
	toaddr = input('жертва:')
	topic = 'спам'
	message = 'вы были заспамлены'
	msg = MIMEMultipart()
	msg[ 'subject' ] = topic
	msg[ 'from' ] = login
	body = message
	msg.attach(MIMEText(body,'plain'))
	server = root.SMTP_SSL(url,465)
	server.login(login,password)
	while True:
		server.sendmail(login,toaddr,msg.as_string())
def main():
	send_email()
if __name__=='__main__':
	main()
