from flask import Flask
import requests

app = Flask(__name__)
apiKeyCode = {}

@app.route('/')
def hello_world():
    res = requests.get('https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=False')
    return 'Hello World!',res.text

if __name__ == '__main__':
    app.run()