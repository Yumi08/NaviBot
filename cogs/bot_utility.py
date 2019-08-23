import discord
from discord.ext import commands

class Bot_Utility(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def info(self, ctx):
        await ctx.send(f'Navi, discord.py, created by {self.client.get_user(218429853144186883)}.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')

    @commands.command()
    async def report(self, ctx, *, message):
        print(f'User report by \"{ctx.author}\": {message}')

    @commands.command()
    @commands.is_owner()
    async def close(self, ctx):
        await ctx.send('Goodbye, Navi.')
        await self.client.close()

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, *, status):
        await self.client.change_presence(activity=discord.Game(status))

def setup(client):
    client.add_cog(Bot_Utility(client))