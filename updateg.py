import discord
from discord.ext import commands

class Updateg:
    def __init__(self, bot):
        self.bot = bot

    async def on_member_update(self, before, after):
        BeforeGame = str(before.game)
        AfterGame = str(after.game)
        if AfterGame != BeforeGame:
            if AfterGame == "DOTA 2":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='dota'))
            if AfterGame == "League of Legends":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='LoL'))
            if AfterGame == "osu!":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='osu!'))
            if AfterGame == "Counter-Strike: Global Offensive":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='cs'))
            if AfterGame == "Hearthstone":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='Hearthstone'))
            if AfterGame == "Heroes of the Storm":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='HOTS'))
            if AfterGame == "Dead by Daylight":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='Dead By Daylight'))
            if AfterGame == "Overwatch":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='Overwatch'))
            if AfterGame == "PUBG":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='PUBG'))
            if AfterGame == "Rocket League":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='Rocket League'))
            if AfterGame == "Grand Theft Auto V":
                await before.add_roles(after, discord.utils.get(after.guild.roles, name='GTA'))

def setup(bot):
    bot.add_cog(Updateg(bot))