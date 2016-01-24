from twilio.rest import TwilioRestClient
import time

account = "AC169cd84f2b74f51bc8abebc42973cb6c"
token = "54ea2786b8eb34dd3dd3a85696233f2d"
client = TwilioRestClient(account, token)

# # Phone numbers
my_number  = '+15418339048'
other_number = '+17189161886'
body_1 = 'Thats play a game Jackie. Do something to stop count down.'
end_body = 'BOOM!!!!!!!!!!!!!!!!!!!!!!!.'
body_count = 'OMG! Dont let the bomb explore.'

# sent a SMS message
for i in range(0, 7):
    if i == 0:
        message = client.messages.create(to=other_number, from_=my_number, body=body_1)
        time.sleep(3)

    elif i == 6:
        time.sleep(6)
        message = client.messages.create(to=other_number, from_=my_number, body=end_body)

    else:
        i = str(6 - i)
        message = client.messages.create(to=other_number, from_=my_number, body=i + '\n' + body_count)
        time.sleep(3)

