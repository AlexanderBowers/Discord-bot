import discord
import os
import requests
import json
from discord.utils import get

client = discord.Client()

member_words = ["erik", "lob", "broomee", "broomeme"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a good person!"]

# def get_quote():
#     response = requests.get("https://zenquotes.io/api/random")
#     json_data = json.loads(response.text)
#     quote = json_data[0]['q'] + " -" + json_data[0]['a']
#     return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'erik' in message.content:
        await message.add_reaction("<:erik:845394606249213992>")

    if 'broomee' in message.content or 'broomeme' in message.content:
        await message.add_reaction("<:broomee:845394578550030386>")
        
    if 'lob' in message.content:
        await message.add_reaction("<:lob:850893095923220530>")
        
        
client.run(os.getenv('TOKEN'))