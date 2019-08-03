import os

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID = os.environ.get('twilio_account')
AUTH_TOKEN  = os.environ.get('twilio_token')
ASSISTANT_SID = os.environ.get('assistant_sid')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

model_build = client.autopilot \
                    .assistants(ASSISTANT_SI) \
                    .model_builds \
                    .create(unique_name='v0.1')

print(model_build.sid)
