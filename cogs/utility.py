import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')

    @commands.command()
    async def report(self, ctx, *, message):
        print(f'User report by \"{ctx.author}\": {message}')

def setup(client):
    client.add_cog(Utility(client))