import discord
from discord.ext import commands

import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Say hello!')
    async def hello(self, ctx):
        await ctx.send(f'Hello, {ctx.author.name}.')

    @commands.command(brief='Magic 8 ball.')
    async def magic8(self, ctx):
        responses = ['Definitely.', 'Without a doubt.', 'Probably.', 'Likely so.', 'Perhaps.', 'Probably not.', 'Unlikely.', 'Definitely not.', 'No way.', 'I don\'t know.', 'I\'m not sure.', 'Ask yourself.']
        await ctx.send(random.choice(responses))
    
    @commands.command(brief='Heads or tails.')
    async def cointoss(self, ctx):
        result = bool(random.getrandbits(1))
        if result:
            await ctx.send("Heads.")
        else:
            await ctx.send("Tails.")

def setup(client):
    client.add_cog(Fun(client))