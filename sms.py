from twilio.rest import Client

accountSID = ''
authToken = ''
twilioClient = Client(accountSID, authToken)
myTwilioNumber = '+1'
myCellPhone = '+1'
message = twilioClient.messages.create(body='', from_=myTwilioNumber, to=myCellPhone)