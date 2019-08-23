import discord
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(brief='Kick user.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command(brief='Ban user.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command(brief='Change a user\'s nickname')
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member : discord.Member, *, nickname):
        await ctx.guild.get_member(member.id).edit(nick=nickname)


def setup(client):
    client.add_cog(Server(client))