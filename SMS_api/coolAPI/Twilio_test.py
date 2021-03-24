# Download the Python helper library from twilio.com/docs/python/install
import os

from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['ACdf1f22c7644584927136b9a6bc22034b']
auth_token = os.environ['7c36300e800db54968b1040cfa19cc22']
client = Client(account_sid, auth_token)
