from flask import Flask
from query_tfl import query_tfl_obj

app = Flask(__name__)
query_obj = query_tfl_obj()
query_obj.main()

@app.route('/')
def hello_world():
    print "TEST"
    return 'Server Index'

if __name__ == '__main__':
    app.run()