from lib.firebase_database import *

async def reputation(message, client):
    user = message.author.id
    rep = firebase_get("rep/" + user)
    if(rep is None):
        await client.send_message(message.channel, "You have no reputation yet")
    else:
        await client.send_message(message.channel, "Your reputation is: " + str(rep['rep']))
