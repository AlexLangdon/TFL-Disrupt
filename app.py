import twilio.twiml
from flask import Flask, request
from query_tfl import query_tfl_obj
import json

app = Flask(__name__)
query_obj = query_tfl_obj()
query_obj.main()

@app.route('/', methods=['POST'])
def handle_POST():
    req_json = json.loads(request.get_data())
    # param = req_json["result"]["parameters"]
    print req_json
    resp = twilio.twiml.Response()
    resp.message("Flask server has received a message")
    return str(resp)

if __name__ == '__main__':
    app.run()