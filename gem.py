import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file('sv_credentials.json')

message = MIMEMultipart()
message['to'] = 'mayalapi@gmail.com'
message['subject'] = 'Subject Line'
body = 'Body of the email'
message.attach(MIMEText(body, 'plain'))

raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')


service = build('gmail', 'v1', credentials=creds)

try:
    send_message = service.users().messages().send(
        userId='me',
        body={'raw': raw_message}
    ).execute()

    print(F'sent message to {message["to"]}')
except TypeError as error:
    print(F'An error occurred: {error}')