import discord
import logging
from discord.ext import commands

import os
import random

logging.basicConfig(level=logging.INFO)

### Region: Vars

client = commands.Bot(command_prefix = '>')

### End: Vars

### Region: Events

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('with Lain'))
    print('Hello, Navi.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('ERROR: Pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('ERROR: Command not found.')
    elif isinstance(error, commands.NotOwner):
        await ctx.send('ERROR: Not server owner.')
    else:
        await ctx.send('ERROR.')

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

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}.')

### End: User commands

# Autoload cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NTg0ODE3NTMxNDU0MjI2NTAz.XV-Awg.hKgssTLIdHwiVK7mqI7K5clB6ew')

