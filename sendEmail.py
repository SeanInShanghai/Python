import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

to = ['XXX@gmail.com']
host = "smtp.gmail.com"
user = "XXXX@gmail.com"
password = "****"



def send_mail(to, subject, content):
	mail_from = user
	
	# send email with attachment
	'''
	msg = MIMEMultipart()
	att1 = MIMEText(open('filepath', 'rb').read(), 'base64', 'gb2312')
	att1["Content-Type"] = 'application/octet-stream'
	att1["Content-Disposition"] = 'attachment; filename="filename"'
	msg.attach(att1)
	'''
	msg = MIMEText(content,_subtype='plain',_charset='gb2312')  # if '_subtype='html'' then send html type e-mail
	msg['Subject'] = subject
	msg['From'] = mail_from
	msg['To'] = ";".join(to)
	
	
	
	try:
		server = smtplib.SMTP()
		server.connect(host)
		server.login(user, password)
		
		server.sendmail(mail_from, to, msg.as_string())
		server.close()
		
		return True
	except Exception, e:
		print(str(e))
		return False

if send_mail(to, "hello subject", "hello content"):
	print("ok")
else:
	print("failed")
		

