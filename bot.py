from threading import Thread
import os.path
import asyncio
import discord
from modules.schoen import schoen
from modules.cadeautjes import cadeautjes
from modules.lekkernijen import lekkernijen
from modules.hulppiet import hulppiet


token = 'NDI1MDA1OTE2MDgyMDEyMTcx.DZBKQg.5y-LPDU7De26AU0to1P0Bj4x-bY'
client = discord.Client()


def logEntry(author, command):
    print('User: "' + author + '" used command: "' + command + '"')


@client.event
async def on_message(message):
    # even zorgen dat marco niet tegen zichzelf gaat kletsen
    if message.author == client.user:
        return

    if message.content.startswith('!schoen'):
        logEntry(message.author.name, message.content)
        await schoen(message, client)

    if message.content.startswith('!cadeautjes'):
        logEntry(message.author.name, message.content)
        await cadeautjes(message, client)

    if message.content.startswith('!lekkernijen'):
        logEntry(message.author.name, message.content)
        await lekkernijen(message, client)

    if message.content.startswith('!hulppiet'):
        logEntry(message.author.name, message.content)
        await hulppiet(message, client)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)