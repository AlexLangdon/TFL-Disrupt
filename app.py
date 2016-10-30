import twilio.twiml
from flask import Flask, request
from query_tfl import query_tfl_obj
import json
import apiai

app = Flask(__name__)
query_obj = query_tfl_obj()
# query_obj.main()

API_AI_CLIENT_TOKEN = "4eb996e7858f44bcb2c6242d112e8517"
ai = apiai.ApiAI(API_AI_CLIENT_TOKEN)

@app.route('/', method=['POST'])
def handle_POST():
    req_json = json.loads(request.get_data())
    # param = req_json["result"]["parameters"]
    # print req_json

    resp = twilio.twiml.Response()
    resp.message("Flask server has received a message")
    return str(resp)

    #
    # aiTest = ai.text_request()
    # aiTest.query = "Get status of victoria"
    # k = aiTest.getresponse()
    # print k.read()
    # return "Beloo"


if __name__ == '__main__':
    app.run()