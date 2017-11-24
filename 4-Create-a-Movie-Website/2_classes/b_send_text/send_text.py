# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

from twilio.rest import TwilioRestClient

# Your code here.
# account sid: AC6fc82bcb1a52f3a0bad38622cbdb1734
# auth token: 6c100bdaff0dd08fea5f60fc73d7d8e8

from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC6fc82bcb1a52f3a0bad38622cbdb1734"
auth_token = "6c100bdaff0dd08fea5f60fc73d7d8e8"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+19195368184",
    from_="+19842047602",
    body="Hello there!")