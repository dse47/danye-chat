from twilio.rest import Client

accountSID = ''
authToken = ''
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+1'
myCellPhone = '+1'
message = twilioCli.messages.create(body='', from_=myTwilioNumber, to=myCellPhone)