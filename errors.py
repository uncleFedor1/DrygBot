import discord
from discord.ext import commands

class CommandErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
        	await ctx.send('Команда не найдена!')
        elif isinstance(error, commands.NoPrivateMessage):
        	await ctx.send('Эта команда не работает в лс!')
        elif isinstance(error, commands.CheckFailure):
        	await ctx.send('У вас недостаточно прав!')

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
