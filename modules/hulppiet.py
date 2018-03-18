from lib.firebase_database import *
import collections

async def hulppiet(message, client):
    user = message.author.id
    counter = 1
    returnString = "```Om je schoen te zetten moet je het volgende doen: \n" \
                   "--  !schoen zetten (hiermee zet je je schoen)\n" \
                   "--  !schoen legen (hiermee haal je je lekkernijen en cadeautjes uit je schoen)\n" \
                   "--  !cadeautjes (hiermee kun je zien wat voor cadeautjes je allemaal al hebt gehad)\n" \
                   "--  !lekkernijen (hiermee kun je zien wat voor lekkernijen je allemaal al hebt gehad)```\n"
    await client.send_message(message.channel,returnString)
    return