from lib.firebase_database import *

async def addrep(message, client):
    author = message.author
    if "pirate lords" in [y.name.lower() for y in author.roles] or "captains" in [y.name.lower() for y in author.roles]:
        addstring = message.content.split()
        if(len(addstring) > 3):
            await client.send_message(message.channel, "You added too many arguments")

        if(len(addstring) < 3):
            await client.send_message(message.channel, "You didn't add enough arguments")
        user = message.mentions[0].id
        amount = addstring[2]
        if(int(amount) < 500):
            rep = firebase_get("rep/" + user)
            if(rep is None):
                firebase_update("rep/" + user, {'rep':amount})
            else:
                firebase_update("rep/" + user, {'rep': int(amount) + int(rep['rep'])})
            await client.send_message(message.channel, "Reputation has succesfully been added")
        else:
            await client.send_message(message.channel, "The amount is too high")
    else:
        await client.send_message(message.channel, "You don't have the rights to add reputation")
