import imaplib, email, getpass
import pandas as pd 


df = pd.DataFrame(columns=['Sender', 'Body'])

user = input("Username: ")
password = getpass.getpass()
imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url)

try:
	con.login(user, password)
except imaplib.IMAP4_SSL.error as e :
	print("LOGIN ERROR : ", e)
	exit(0)

con.select('Inbox')

rv, data = con.search(None, '(SINCE "26-May-2020")')
msgs = []

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
for latest_email_id in id_list:

	result, data = con.fetch(latest_email_id, "(RFC822)") 

	raw_email = data[0][1] 
	raw_email_string = raw_email.decode('utf-8')

	
	msg = email.message_from_string(raw_email_string)
	print(str(msg['From']))
	sender = str(msg['From'])
	for part in msg.walk():
		if part.get_content_type()=="text/plain":
			body = part.get_payload(decode=True)
			body = body.decode('utf-8')
			body = body.rstrip()
			print(body)
			body = body.replace('\r','')
			body = body.replace('\n','')
			

	df = df.append({'Sender' : sender, 'Body' : body}, ignore_index=True)
	



	print("\n\n\n\n")



print(df)
df.to_csv('mails.csv')	

con.close()
print('connection closed')
con.logout()
print("LOGGED OUT")
