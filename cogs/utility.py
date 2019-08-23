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

    @commands.command()
    async def close(self, ctx):
        if ctx.author.id == 218429853144186883:
            await ctx.send('Goodbye, Navi.')
            await self.client.close()
        else:
            await ctx.send('You\'re not Yumi.')

    @commands.command()
    async def status(self, ctx, *, status):
        await self.client.change_presence(activity=discord.Game(status))

def setup(client):
    client.add_cog(Utility(client))