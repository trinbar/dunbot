# os library allows access to environment variables stored in .gitignore
# Please secure your own Twilio Account SID and Auth Token
import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
ACCOUNT_SID = os.environ.get('twilio_account')
AUTH_TOKEN  = os.environ.get('twilio_token')
ASSISTANT_SID = os.environ.get('assistant_sid')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

"""
## Build task actions that say something and listens for a response. ##

** create_greet.py is the default task action **
** default actions initiate and act as a fallback **

See https://www.twilio.com/docs/autopilot/actions

Actions are how you program the Tasks that your Autopilot virtual assistant performs. 
Actions will be executed once a user invokes a Task during the dialogue. 
A user can land on a task by being routed by the natural language router 
   or by being redirected from another task.

Actions can be any of the following:
:say - instructs Autopilot what to speak or text back to the end user.
:collect - instructs Autopilot to collect data from the user in a conversational form.
:listen -instructs Autopilot listen for user input, perform the 
    natural language analysis and route to the corresponding task.
:redirect - instructs Autopilot to redirect the Dialogue to the specified task.
:handoff - hands off the session to a TwiML voice URL or TaskRouter queue.
:remember - instructs Autopilot to store a key-value pair.
:show - instructs Autopilot to render back visual content to devices with screens.
"""


greet_task_actions = {
    'actions': [
        {'say': 'Hola!, I\'m Dunbot, your virtual assistant! How can I help you?'},
        {'listen': True}
    ]
}

# Create the greet task
task = client.autopilot.assistants(ASSISTANT_SID) \
                       .tasks \
                       .create(
                           unique_name='greet',
                           actions=greet_task_actions)

print("Greet task has been created!")
print(task.sid)
