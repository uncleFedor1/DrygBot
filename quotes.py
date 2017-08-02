import discord
import datetime
from discord.ext import commands

class Quotes:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def quote(self, ctx, message):
        ch = ctx.message.channel
        msg = await ch.get_message(message)
        embed = discord.Embed(title=None, description=msg.content, colour=msg.author.color)
        embed.set_author(name=msg.author.name + '#' + msg.author.discriminator, icon_url=msg.author.avatar_url)
        embed.set_footer(text='ID сообщения: ' + str(ctx.message.id))
        await ctx.message.delete()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Quotes(bot))