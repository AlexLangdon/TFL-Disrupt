from twilio.rest import TwilioRestClient
from flask import Flask, request
from query_tfl import query_tfl_obj
import twillio_tokens

app = Flask(__name__)
client = TwilioRestClient(twillio_tokens.account_sid,
                          twillio_tokens.auth_token)

@app.route('/')
def sms_in() :
    from_number = request.values.get('From', None)
    text_body = request.values.get('Body', None)