import discord
import requests
import logging
import random
import settings
from discord.ext.commands import Bot

logging.basicConfig(level=logging.WARNING)

client = Bot(command_prefix=settings.BOT_PREFIX)

@client.command(name='8', description='Answers a yes/no question', brief='Answers from the beyond', aliases=['8ball','eightball'], pass_context=True)
async def eight_ball(context):
    responses = [
        'As I see it, yes',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don’t count on it',
        'It is certain',
        'It is decidedly so',
        'Most likely',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Outlook good',
        'Signs point to yes',
        'Very doubtful',
        'Without a doubt',
        'Yes',
        'Yes – definitely',
        'You may rely on it'
    ]
    await context.send(random.choice(responses) + ", " + context.message.author.mention)

@client.command(pass_context=True)
async def bitcoin(context):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await context.send('Bitcoin price is: $' + value)

@client.command(name='group', pass_context=True)
async def tp_group(context):
    url = 'https://tagpro.koalabeast.com/groups/create'
    response = requests.post(url)
    await context.send(response.url)

client.run(settings.DISCORD_TOKEN)
