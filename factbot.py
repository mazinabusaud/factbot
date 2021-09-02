#importing discord package
import discord
from better_profanity import profanity
import random

#client (the bot)
client=discord.Client()
#do what bot doesssss
@client.event

async def on_message(message):
    messageContent=message.content
    #checking if its boat
    me = <commander id>
    if message.author.id == me:
        if 'tar.get' in messageContent:
            global target 
            target = message.mentions[0].id
            await message.channel.send('Target Acquired: <@{}>'.format(target))
    if message.author.id == target:
            if profanity.contains_profanity(messageContent):
                await message.delete()
                await message.channel.send('You said a no no word <@{}>'.format(target))
    if 'do.it' in messageContent:
        await message.channel.send('<@{}> {}'.format(target, random.choice(open('facts.txt').readlines())))
#run on server, put token in parentheses
client.run('')

