from twilio.rest import Client

accountSID = 'ACa8edc29a571e8e41969bcf6e35aee273'

AuthToken = '072d9fce0bd2d4913d750d53a73a906d'

client = Client(accountSID, AuthToken)

TwilioNumber = '+14843107924'

mycellphone = '+14154196778'

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body='Hello World!')


print(textmessage.status)

call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to=mycellphone, from_=TwilioNumber)
