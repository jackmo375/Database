#
#	SICKLE IN AFRICA step 4
#
#	email data cleaning reports
#	Author: Wilson Mupfururirwa
#
####################################

import sys, argparse

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


def main():

	args = getShellArguments()

	attachmentPath = args.repDir + 'cleaningReport.long.txt'

	msg = MIMEMultipart() 

	msg['From'] = args.fromAdd 

	msg['To'] = args.toAdd

	msg['Subject'] = "Mail"

	body = '''
	Dear SIA member

	please find enclosed the data cleaning report from SADaCC.

	Kind regards,
	the SADaCC team
	'''

	msg.attach(MIMEText(body, 'plain')) 

	filename = 'cleaningReport.long.txt'
	attachment = open(attachmentPath, "rb") 

	p = MIMEBase('application', 'octet-stream') 

	p.set_payload((attachment).read())

	encoders.encode_base64(p)

	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(p)

	s = smtplib.SMTP('smtp.gmail.com', 587) 

	s.starttls() 

	s.login(args.fromAdd, args.fromPswd) 

	text = msg.as_string() 

	s.sendmail(args.fromAdd, args.toAdd, text)
	print("Success!")

	s.quit()



def getShellArguments():
	'''
	Get shell enviroment arguments
	'''
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'--repDir',
		type=str,
		help='path to temporary quality reports storage directory')
	parser.add_argument(
		'--fromAdd',
		type=str,
		help='email address of cleaning report *sender*')
	parser.add_argument(
		'--fromPswd',
		type=str,
		help='email account password of cleaning-report sender')
	parser.add_argument(
		'--toAdd',
		type=str,
		help='email address of cleaning report *receiver*')

	return parser.parse_args()


if __name__ == '__main__':
	main()