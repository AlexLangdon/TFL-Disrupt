import requests

def main() :
    query_tfl()

def query_tfl() :
    res = requests.get('https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=False')
    print res.json()