from flask import Flask
import query_tfl

app = Flask(__name__)
query_tfl.main()

@app.route('/')
def hello_world():
    return 'Server Index'

if __name__ == '__main__':
    app.run()