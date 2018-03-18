import discord
from modules.addrep import addrep
from modules.subrep import subrep
from modules.ranks import ranks
from modules.reputation import reputation


token = ''
client = discord.Client()


def logEntry(author, command):
    print('User: "' + author + '" used command: "' + command + '"')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!addrep'):
        logEntry(message.author.name, message.content)
        await addrep(message, client)

    if message.content.startswith('!subrep'):
        logEntry(message.author.name, message.content)
        await subrep(message, client)

    if message.content.startswith('!ranks'):
        logEntry(message.author.name, message.content)
        await ranks(message, client)

    if message.content.startswith('!reputation'):
        logEntry(message.author.name, message.content)
        await reputation(message, client)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)
