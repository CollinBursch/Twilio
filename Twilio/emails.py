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

'''
        # Auto reply
        if 'absence' in message.subject:
            print('Found message with absence')

            Msg = outlook.CreateItem(0)
            Msg.Importance = 1
            Msg.Subject = 'Got your ' + message.subject + ' email'
            Msg.HTMLBody = 'Hi' + message.sender +'\n' ' sorry you are not well'

            Msg.To = message.sender.GetExchangeUser().PrimarySmtAddress
            Msg.ReadReciptRequested = True 

            Msg.Send()
'''