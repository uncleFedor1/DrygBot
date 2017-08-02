import discord
import datetime
from discord.ext import commands

class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, *, msg: str):
        await self.bot.change_presence(game=discord.Game(name=msg))
        x = 'Статус обновлен на `{}`'.format(msg)
        e = discord.Embed(title=None, description=x)
        await ctx.send(embed=e, delete_after=10.0)

    @commands.command()
    @commands.is_owner()
    async def resetstatus(self, ctx):
        await self.bot.change_presence(game=discord.Game(name=None))
        e = discord.Embed(title=None, description='Статус сброшен')
        await ctx.send(embed=e, delete_after=10.0)

def setup(bot):
    bot.add_cog(Admin(bot))