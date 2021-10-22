from twilio.rest import Client
from config import auth

def send_message(cod):
	client = Client(auth['account_sid'], auth['auth_token'])

	message = client.messages.create(
		to="+5538992251157", 
		from_="+13348100426",
		body=f"Seu código de verificação é {cod}"
	)