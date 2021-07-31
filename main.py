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

    if 'erik ' in message.content or 'turoths' in message.content:
        await message.add_reaction("<:just_erik_things:454520448655294474>")

    if 'broomee' in message.content or 'broomeme' in message.content:
        await message.add_reaction("<:just_broomeme_things:619182175488704512>")
        
    if ' lob ' in message.content:
        await message.add_reaction("<:just_lob_things:464553024308772895>")

    if message.content == '!raksha guide':
        guide = 'https://www.youtube.com/watch?v=6LROlMZmC3w'
        await message.channel.send(guide)
    
    if message.content == '!quests':
        link = 'https://runescape.wiki/w/Quests'
        await message.channel.send(link)
    
    if message.content == '!comp':
        link = 'https://runescape.wiki/w/Completionist_Cape_(achievement)'
        await message.channel.send(link)
    
    if message.content == '!revo':
        guide = 'https://runescape.wiki/w/Revolution/Bars#Revolution++_bars'
        await message.channel.send(guide)
    
    if message.content == '<@261773632609452033>':
        ping = "<:ping:868547282574929930>"
        await message.channel.send(ping)

    if 'i died' in message.content:
        response = 'git gud'
        await message.channel.send(response)
    
    if message.content == '@oddments':
        response = 'thank you, erik'
        await message.channel.send(response)

client.run(os.getenv('TOKEN'))