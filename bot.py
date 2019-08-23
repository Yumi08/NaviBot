import discord
from discord.ext import commands

import os
import random

### Region: Vars

client = commands.Bot(command_prefix = '.')

### End: Vars

### Region: Events

@client.event
async def on_ready():
    print('Hello, Navi.')

@client.event
async def on_command_error(ctx, error):
    await ctx.send('Error.')

### End: Events

### Region: User commands

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}.')

### End: User commands

# Autoload cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NTg0ODE3NTMxNDU0MjI2NTAz.XV-Awg.hKgssTLIdHwiVK7mqI7K5clB6ew')

