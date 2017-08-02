import discord
import datetime
from discord.ext import commands

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        await ctx.send(message)
        
def setup(bot):
    bot.add_cog(Fun(bot))