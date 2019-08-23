import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

client.run('NTg0ODE3NTMxNDU0MjI2NTAz.XV-Awg.hKgssTLIdHwiVK7mqI7K5clB6ew')

