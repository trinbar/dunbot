# os library allows access to environment variables stored in .gitignore
# Please secure your own Twilio Account SID and Auth Token
import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID = os.environ.get('twilio_account')
AUTH_TOKEN  = os.environ.get('twilio_token')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

assistant = client.autopilot \
                  .assistants \
                  .create(
                       friendly_name='Quickstart Assistant',
                       unique_name='quickstart-assistant'
                   )

print(assistant.sid)
