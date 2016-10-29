from twilio.rest import TwilioRestClient

account_sid = "AC9df38f3b52ce616f29a661463ed82f91" # Your Account SID from www.twilio.com/console
auth_token  = "ca57daf1e7bb1b4a2dfba2b9b936e6c2"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)


def sms_out(text, nums):
    for x in xrange(len(nums)) :
        message = client.messages.create(body=text,
                                         to=nums[x],    # Replace with your phone number
                                         from_="+441158245082") # Our Twilio number
        #print(message.sid)
    return
    # Input is a text string to be sent to an array of numbers

# Test array of phone numbers
phone_numbers = ["+447805081856","+447480132452","+447515067000","447739586816","+447809358784"]

# Pass array and message to function
sms_out("Hello from BrumHack", phone_numbers)