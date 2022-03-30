import win32com.client
from twilio.rest import Client

outlook = win32com.client.Dispatch('Outlook.Application')
outlook_ns = outlook.GetNamespace('MAPI')

myfolder = outlook_ns.Folders['collin_bursch1@baylor.edu'].Folders['Inbox']

messages = myfolder.Items

messagescount = 0

for message in messages:
    if message.UnRead:
        print(message.sender)
        print(message.subject)
        messagescount += 1
print(messagescount)



accountSID = 'ACa8edc29a571e8e41969bcf6e35aee273'

AuthToken = '072d9fce0bd2d4913d750d53a73a906d'

client = Client(accountSID, AuthToken)

TwilioNumber = '+14843107924'

mycellphone = '+14154196778'

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body=str('messagescount')


# print(textmessage.status)

# call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to=mycellphone, from_=TwilioNumber)