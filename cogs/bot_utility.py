import discord
from discord.ext import commands

class Bot_Utility(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(brief='Get bot info.')
    async def info(self, ctx):
        await ctx.send(f'<:navi:614422620540108801> discord.py, created by {self.client.get_user(218429853144186883)}.')

    @commands.command(brief='Get bot latency.')
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')

    @commands.command(brief='Report a bug to the developer.')
    async def report(self, ctx, *, message):
        print(f'User report by \"{ctx.author}\": {message}')

    @commands.command(brief='OWNER ONLY: Close bot.')
    @commands.is_owner()
    async def close(self, ctx):
        await ctx.send('Goodbye, Navi.')
        await self.client.close()

    @commands.command(brief='OWNER ONLY: Set bot status.')
    @commands.is_owner()
    async def status(self, ctx, *, status):
        await self.client.change_presence(activity=discord.Game(status))

def setup(client):
    client.add_cog(Bot_Utility(client))