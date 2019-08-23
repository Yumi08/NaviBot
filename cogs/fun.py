import discord
from discord.ext import commands

import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        responses = ['Definitely.', 'Probably.', 'Perhaps.', 'Probably not.', 'Definitely not.']
        await ctx.send(random.choice(responses))

def setup(client):
    client.add_cog(Fun(client))