# https://github.com/Biggkahuna98/bigg-discord-bot/blob/master/shrekbot.py
import discord

TOKEN = 'NDY4OTM4MzQ4Nzk5NDU5MzI4.DjAeaw.cvTXnHuffxFEeuo1OhRB5arACAE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)