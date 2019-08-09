import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, sys, getpass
from time import sleep

def banner():

	os.system("clear")
	print ("""\033[1;32m

	   ____            __           _ __
	  / __/__ ___  ___/ /_ _  ___ _(_) /
	 _\ \/ -_) _ \/ _  /  ' \/ _ `/ / /
	/___/\__/_//_/\_,_/_/_/_/\_,_/_/_/
		""")
banner()

try:

	def gmail():
		#The mail addresses and password
		sender_address = raw_input("\033[1;33m[+]\033[1;31m Email kamu:\033[1;36m ")
		if not sender_address:
			exit("\033[1;35m	[x]\033[1;32m Login dibutuhkan")
		sender_pass = getpass.getpass("\033[1;33m[+]\033[1;31m Password: ")
		if not sender_pass:
			exit("\033[1;35m	[x]\033[;32m Login dibutuhkan")
		receiver_address = raw_input("\033[1;33m[+]\033[1;31m Receiver Mail:\033[1;36m ")
		mail_content = raw_input("\n\033[1;31m	[+]\033[1;33m Pesan:\n\033[1;37m	>\033[1;35m ")
		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = raw_input("\033[1;31m	[+]\033[1;33m Subject:\n\033[1;37m	>\033[1;35m ")   #The subject line
		#The body and the attachments for the mail
		message.attach(MIMEText(mail_content, 'plain'))
		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print ("\033[1;31m[+]\033[1;33m Pesan berhasil dikirim..")
	gmail()
except KeyboardInterrupt:
	print ("\033[1;31m[+]\033[1;33m Good byee..")
except Exception:
	print ("\n\033[1;31m[!]\033[1;33m Login Gagal. Mohon Aktifkan Sumber Aplikasi tidak dikenal");print ("\033[1;31m[+]\033[1;33m Mengarahkan ke sumber dalam 10 detik..");sleep(0.10);os.system("termux-open https://myaccount.google.com/lesssecureapps?utm_source=google-account&utm_medium=web")
