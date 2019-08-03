import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID = os.environ.get('twilio_account')
AUTH_TOKEN  = os.environ.get('twilio_token')
ASSISTANT_SID = os.environ.get('assistant_sid')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

defaults = client.autopilot \
                 .assistants(ASSISTANT_SID) \
                 .defaults() \
                 .update(defaults={
                      'defaults': {
                          'assistant_initiation': 'task://greet',
                          'fallback': 'task://greet'
                      }
                  })

print(defaults.assistant_sid)
