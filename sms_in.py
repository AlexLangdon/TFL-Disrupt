from twilio.rest import TwilioRestClient
from flask import Flask, request
from query_tfl import query_tfl_obj

app = Flask(__name__)

account_sid = "AC9df38f3b52ce616f29a661463ed82f91" # Your Account SID from www.twilio.com/console
auth_token  = "ca57daf1e7bb1b4a2dfba2b9b936e6c2"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

@app.route('/')
def sms_in() :
    from_number = request.values.get('From', None)
    text_body = request.values.get('Body', None)