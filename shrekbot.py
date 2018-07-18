# https://github.com/Biggkahuna98/bigg-discord-bot/blob/master/shrekbot.py
import discord
import asyncio
import random

TOKEN = 'NDY4OTM4MzQ4Nzk5NDU5MzI4.DjAeaw.cvTXnHuffxFEeuo1OhRB5arACAE'

client = discord.Client()

@client.event
async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='468944647041843201')
    possible_responses = [
        'I am the Ogrelord motherfuckers! Bow to my greatness',
        'Fuckin\' donkey!!',
        'GET OUT OF MY SWAMP!!!!',
        'NOM NOM NOM NOM I WILL EAT ALL OF YOU!'
    ]
    while not client.is_closed:
        await client.send_message(channel, random.choice(possible_responses))
        await asyncio.sleep(5)

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}! Enjoy your stay motherfucker.'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello') and discord.Object(id='468944647041843201'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run(TOKEN)