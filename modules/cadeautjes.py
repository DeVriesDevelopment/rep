from lib.firebase_database import *
import collections

async def cadeautjes(message, client):
    user = message.author.id
    counter = 1
    returnString = "```Sinterklaas heeft jou de volgende cadeautjes gegeven: \n"
    cadeaus = firebase_get('schoentjes/' + user + '/cadeautjes')
    if(cadeaus is None):
        returnString += "Nog niks"
        returnString += "```"
    else:
        cadeaus = collections.OrderedDict(reversed(list(cadeaus.items())))
        for key, value in cadeaus.items():
            returnString += str(counter) + '. ' + list(value.keys())[0] + '\n'
            counter += 1
        returnString += "```"
    await client.send_message(message.channel,returnString)
    return