import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'erik' in message.content:
        await message.add_reaction("<:just_erik_things:454520448655294474>")

    if 'broomee' in message.content or 'broomeme' in message.content:
        await message.add_reaction("<:just_broomeme_things:845394578550030386>")
        
    if 'lob' in message.content:
        await message.add_reaction("<:just_lob_things:850893095923220530>")
        
        
client.run(os.getenv('TOKEN'))