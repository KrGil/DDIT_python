# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACdf1f22c7644584927136b9a6bc22034b']
auth_token = os.environ['7c36300e800db54968b1040cfa19cc22']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='eng',
                              from_='+15512240680',
                              to='+8201039350724'
                          )

print(message.sid)