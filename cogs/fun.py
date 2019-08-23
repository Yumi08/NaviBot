import discord
from discord.ext import commands

import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello, {ctx.author.name}.')

    @commands.command()
    async def magic8(self, ctx):
        responses = ['Definitely.', 'Without a doubt.', 'Probably.', 'Likely so.', 'Perhaps.', 'Probably not.', 'Unlikely.', 'Definitely not.', 'No way.', 'I don\'t know.', 'I\'m not sure.', 'Ask yourself.']
        await ctx.send(random.choice(responses))

def setup(client):
    client.add_cog(Fun(client))