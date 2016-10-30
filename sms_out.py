from twilio.rest import TwilioRestClient
import twillio_tokens

class sms_out_obj():
    client = TwilioRestClient(twillio_tokens.account_sid,
                              twillio_tokens.auth_token)

    def send_sms(self, text, nums):
        for x in xrange(len(nums)) :
            message = self.client.messages.create(body=text,
                                             to=nums[x],    # Replace with your phone number
                                             from_="+441158245082") # Our Twilio number
            #print(message.sid)
        return
        # Input is a text string to be sent to an array of numbers

    # Test array of phone numbers
    #phone_numbers = ["+447805081856","+447480132452","+447515067000","447739586816","+447809358784"]
    # Pass array and message to function
    #send_sms("Hello from BrumHack", phone_numbers)