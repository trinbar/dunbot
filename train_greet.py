import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
ACCOUNT_SID = os.environ.get('twilio_account')
AUTH_TOKEN  = os.environ.get('twilio_token')
ASSISTANT_SID = os.environ.get('assistant_sid')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

greetings = [
    'hello',
    'hi',
    'Hello',
    'Hi there',
    'Hola',
    'Sup',
    'Yo'
]

for greeting in greetings:
    sample = client.autopilot \
        .assistants(ASSISTANT_SID) \
        .tasks('greet') \
        .samples \
        .create(language='en-us', tagged_text=greeting)

    print(sample.sid)
