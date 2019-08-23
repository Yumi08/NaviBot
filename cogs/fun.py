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
    
    @commands.command(brief='Mention someone random.')
    async def someone(self, ctx):
        await ctx.send(f'{random.choice(ctx.guild.members).mention}')

    @commands.command(brief='Send an anonymous message to someone.')
    async def whisper(self, ctx, user : discord.User, *, message):
        await user.send(f'Someone whispers to you: "{message}".')
        await ctx.message.delete()

    @commands.command(brief='Send a not-so-anonymous message to someone.')
    async def yell(self, ctx, user : discord.User, *, message):
        await user.send(f'{ctx.author.mention} yells to you: "{message}".')
        await ctx.message.delete()
        

def setup(client):
    client.add_cog(Fun(client))