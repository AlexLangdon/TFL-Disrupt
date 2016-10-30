from twilio.rest import TwilioRestClient
from flask import Flask, request
import apiai
import twillio_tokens
import json

app = Flask(__name__)
client = TwilioRestClient(twillio_tokens.account_sid,
                          twillio_tokens.auth_token)

API_AI_CLIENT_TOKEN = "4eb996e7858f44bcb2c6242d112e8517"
ai = apiai.ApiAI(API_AI_CLIENT_TOKEN)

def get_line(self, apiai_json) :
    line_py_obj = json.dumps(apiai_json)
    line = line_py_obj["result"]["parameters"]["line"]
    return line

def sms_in() :
    from_number = request.values.get('From', None)
    text_body = request.values.get('Body', None)

    aiGetLine = ai.text_request()
    aiGetLine.query = text_body
    resp = aiGetLine.getResponse()

    alert_request = [from_number, get_line(resp)]
    return alert_request


