# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

token = client.tokens.create()
print token.username