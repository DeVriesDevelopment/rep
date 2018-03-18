from lib.firebase_database import *
import discord
import operator

ranks = {0: "Crew Member", 15:"Buccaneers", 50:"Quartermasters", 100: "First Mates", 150: "Captains"}
forRanks = sorted(ranks.items(), key=operator.itemgetter(0))
async def addrep(message, client):
    author = message.author
    if "pirate lords" in [y.name.lower() for y in author.roles] or "captains" in [y.name.lower() for y in author.roles]:
        addstring = message.content.split()
        if(len(addstring) > 3):
            await client.send_message(message.channel, "You added too many arguments")

        if(len(addstring) < 3):
            await client.send_message(message.channel, "You didn't add enough arguments")
        user = message.mentions[0].id
        realUser = message.mentions[0]
        amount = addstring[2]
        if(int(amount) < 500):
            rep = firebase_get("rep/" + user)
            if(rep is None):
                firebase_update("rep/" + user, {'rep':amount})
            else:
                firebase_update("rep/" + user, {'rep': int(amount) + int(rep['rep'])})

            rep = firebase_get("rep/" + user)
            rep = int(rep['rep'])
            currentRank = 0
            for rank in forRanks:
                if(rank[0] <= rep):
                    currentRank = rank[0]
            for tmpRole in message.server.roles:
                if(tmpRole.name == ranks.get(currentRank)):
                    role = tmpRole
            await client.add_roles(realUser, role)
            await client.send_message(message.channel, "Reputation has succesfully been added")
        else:
            await client.send_message(message.channel, "The amount is too high")
    else:
        await client.send_message(message.channel, "You don't have the rights to add reputation")
