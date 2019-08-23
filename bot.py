import discord
from discord.ext import commands

import random

### Region: Vars

client = commands.Bot(command_prefix = '.')

### End: Vars

### Region: Events

@client.event
async def on_ready():
    print('Bot ready.')

@client.event
async def on_command_error(ctx, error):
    await ctx.send("Error.")

### End: Events

### Region: User commands

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx):
    responses = ['Definitely.', 'Probably.', 'Perhaps.', 'Probably not.', 'Definitely not.']
    await ctx.send(random.choice(responses))

@client.command()
async def report(ctx, *, message):
    print(f'User report by \"{ctx.author}\": {message}')

### End: User commands

client.run('NTg0ODE3NTMxNDU0MjI2NTAz.XV-Awg.hKgssTLIdHwiVK7mqI7K5clB6ew')

