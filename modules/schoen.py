import requests
import json
import datetime
import string
import random
from dateutil.relativedelta import relativedelta
import time
from lib.firebase_database import *


lekkernijen = [
'Taai-taai',
'Kruidnoten',
'Schuimpjes',
'Borstplaat',
'Een zakje Kikkers en muizen',
'Marsepein',
'Pepernoten',
'Chocolade munten',
'Speculaasjes',
'Gevulde speculaas',
'Speculaasbrokken',
'Chocoladekruidnoten',
'Amandelstaaf',
'Pure chocoladeletter',
'Witte chocoladeletter',
'Melk chocoladeletter'

];
cadeautjes = [
'een goocheldoos',
'een constructieset voor een Takelwagen',
'Pink City Geluksarmbandjes',
'een Bouwblokken Speelset',
'een constructieset Kraanwagen',
'een verkleedset Vlinder - Paars',
'een speelgoed Terreinwagen',
'een Spy Voice Recorder Pen',
'Bruynzeel Magische Stiften',
'het spel Vang de Rat',
'het spel Mikado XL',
'Danslint',
'een Stapeltoren 9-delig',
'een 12 in 1 Spellendoos',
'een Camouflage Verrekijker',
'een Vang - Werpspel Klittenband',
'een Fidget spinner',
'een Opblaasbare bokszak',
'een Opblaasbare flamingo',
'Sokken',
'een Bellenblaasmachine',
'een Iphone X 256GB',
'een Pak speelkaarten',
'Eenhoorn sloffen',
'een mok',
'Monopoly geld',
'Elly en Rikkerts "Een boom vol liefde"',
'een leven'
];

async def schoen(message, client):
    param = message.content.replace('!schoen ', '')
    if(param == 'zetten'):
        await zet_schoen(message, client)

    if(param == "legen"):
        await leeg_schoen(message, client)




async def zet_schoen(message, client):
    user = message.author.id
    data = {'gezet':1,
            'gezet_tijd':int(time.time())}
    if(firebase_get('schoentjes/' + user + '/gezet') == 1):
        await client.send_message(message.channel, 'Je hebt je schoentje al gezet. Je kan maar 1 schoentje zetten jij gierig joch!')
        return
    else:
        firebase_update('schoentjes/' + user, data)
        await client.send_message(message.channel, 'Je hebt je schoentje gezet. Nu hopen dat de Sint vanavond langskomt.')
        return


async def leeg_schoen(message, client):
    user = message.author.id
    data = {'gezet': 0}
    lekkernij = random.choice(lekkernijen)
    if("chocoladeletter" in lekkernij):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letter = random.choice(letters)
        lekkernij = lekkernij + " (letter " + letter + ")"
    cadeautje = random.choice(cadeautjes)
    sweet_data = {lekkernij : 1}
    present_data = {cadeautje: 1}
    if (firebase_get('schoentjes/' + user + '/gezet') == 1):
        gezette_tijd = datetime.datetime.fromtimestamp(int(firebase_get('schoentjes/' + user + '/gezet_tijd')))
        _3AM = datetime.time(hour=3)
        if(gezette_tijd.time() < _3AM):
            threshold = gezette_tijd.replace(hour=3, minute=0, second=0)
        else:
            threshold = gezette_tijd + datetime.timedelta(days=1)
            threshold = threshold.replace(hour=3, minute=0, second=0)
        print(int(threshold.strftime("%s")))
        if(int(time.time()) > int(threshold.strftime("%s"))):
            firebase_update('schoentjes/' + user, data)
            firebase_create('schoentjes/' + user + '/cadeautjes', present_data, True)
            firebase_create('schoentjes/' + user + '/lekkernijen', sweet_data, True)
            await client.send_message(message.channel, 'De sint heeft je schoentje gevuld! Je hebt ' + lekkernij + ' en ' + cadeautje + ' gekregen.')
            return
        else:
            await client.send_message(message.channel,'De sint is nog niet langs geweest. Even geduld jij!')
            return
    else:
        await client.send_message(message.channel, 'Je hebt je schoentje nog niet gezet, doe het snel!')
        return