import discord
from discord.ext import commands

import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx):
    responses = ['Definitely.', 'Perhaps.', 'Definitely not.']
    await ctx.send(random.choice(responses))

client.run('NTg0ODE3NTMxNDU0MjI2NTAz.XV-Awg.hKgssTLIdHwiVK7mqI7K5clB6ew')

