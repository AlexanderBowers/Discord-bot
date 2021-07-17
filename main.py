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
        await message.add_reaction("<:just_broomeme_things:619182175488704512>")
        
    if 'lob' in message.content:
        await message.add_reaction("<:just_lob_things:464553024308772895>")

    if message.content == '!raksha guide':
        guide = 'https://www.youtube.com/watch?v=6LROlMZmC3w'
        await message.channel.send(guide)
    
    if message.content == '!revo':
        guide = 'https://runescape.wiki/w/Revolution/Bars#Revolution++_bars'
        await message.channel.send(guide)

client.run(os.getenv('TOKEN'))