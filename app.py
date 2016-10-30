import twilio.twiml
from flask import Flask, request, Response
from query_tfl import query_tfl_obj
import json
import apiai
import sys

app = Flask(__name__)
query_obj = query_tfl_obj()
query_obj.main(False)

# API_AI_CLIENT_TOKEN = "4eb996e7858f44bcb2c6242d112e8517"
# ai = apiai.ApiAI(API_AI_CLIENT_TOKEN)

@app.route('/', methods=['GET'])
def handle_GET():
    return "Default response."

@app.route('/', methods=['POST'])
def handle_POST():
    req_json = json.loads(request.get_data())
    print req_json
    # sys.stdout.flush()

    result = req_json["result"]
    intent = result["metadata"]["intentName"]

    if intent == "Registration" :
        print "Registering"
        print query_obj.db_obj.db_store
        phone_num = result["parameters"]["phone-number"]
        query_obj.db_obj.add_num("circle",phone_num)
        query_obj.send_status(phone_num,"circle")

    if intent == "Set alert" :
        print "Seting alert"
        print query_obj.db_obj.db_store
        phone_num = result["parameters"]["phone-number"]
        line = result["parameters"]["line"]
        query_obj.db_obj.add_num(line,phone_num)
        query_obj.send_status(phone_num,line)

    if intent == "Check for disruptions" :
        print "Checking for disruptions"
        line = result["parameters"]["line"]
        text = query_obj.get_status(line)

        resp_obj = {}
        resp_obj['speech'] = text
        resp_obj['displayText'] = text
        resp_obj['data'] = {}
        resp_obj['contextOut'] = []
        resp_obj['source'] = 'Me'
        json_out = json.dumps(resp_obj)
        return Response(response=json_out, status=200, mimetype="application/json")

    # resp = twilio.twiml.Response()
    # resp.message("Flask server has received a message")

    # aiTest = ai.text_request()
    # aiTest.query = "Get status of victoria"
    # k = aiTest.getresponse()
    # print k.read()

    # return str(resp)

if __name__ == '__main__':
    app.run()