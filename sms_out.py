from twilio.rest import TwilioRestClient

def test():
    account_sid = "ACXXXXXXXXXXXXXXXXX"
    auth_token = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(account_sid, auth_token)

def sms_in():
    return

def sms_out(text, nums):
    return
    # Input is a text string to be sent to an array of numbers