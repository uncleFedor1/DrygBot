from discord.ext import commands

import discord
import random
import datetime

description = '''shitbot'''

startup_extensions = ["cogs.admin", "cogs.updateg", "cogs.quotes", "cogs.fun"]

bot = commands.Bot(command_prefix='#', description=description)
bot.remove_command('help')

print('Connecting...')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='All For You'))

@bot.command()
async def anon(ctx, *, msg: str):
    channel = discord.utils.get(bot.get_all_channels(), name='anon_friend')
    em = discord.Embed(title=None, description=msg, timestamp = datetime.datetime.utcnow(), colour=0x6c85ff)
    em.set_author(name='Anonymous', icon_url='https://i.imgur.com/jbTMFWK.png')
    emb = discord.Embed(title='📬 Отправлено!', description='Ваше анонимное сообщение было отправлено.', colour=0x6c85ff)
    await channel.send(embed=em)
    await ctx.send(embed=emb, delete_after=10.0)
    if isinstance(ctx.channel, discord.abc.GuildChannel):
        await ctx.message.delete()
    else:
        pass

@bot.command()
async def sinfo(ctx):
    e = discord.Embed(title=None, description=None, colour=0x6c85ff)
    e.add_field(name='Название сервера', value=ctx.guild.name)
    e.add_field(name='Владелец сервера', value=ctx.guild.owner)
    e.add_field(name='Дата создания', value="{}".format(ctx.guild.created_at.strftime('%a %d %b %Y at %H:%M')))
    e.add_field(name='Кол-во участников', value=ctx.guild.member_count)
    e.add_field(name='Регион', value=ctx.guild.region)
    e.set_footer(text='ID сервера: ' + str(ctx.guild.id))
    e.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=e)

@bot.command()
async def uinfo(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.message.author
    e = discord.Embed(title=None, description=None, colour=0x6c85ff)
    e.add_field(name='Имя', value='**{}**'.format(member.name) + '#' + member.discriminator)
    e.add_field(name='Дата регистрации', value="{}".format(member.created_at.strftime('%d %b %Y at %H:%M')))
    e.add_field(name='Присоединился к серверу', value=member.joined_at.strftime('%d %b %Y at %H:%M'))
    e.add_field(name='Игра', value=member.game)
    e.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=e)

@bot.command()
async def report(ctx, *, msg: str):
    channel = discord.utils.get(bot.get_all_channels(), name='reports')
    author = ctx.message.author
    if channel is None:
        e = discord.Embed(title=None, description='❌ Канала для жалоб не существует.', colour=0x6c85ff)
        await ctx.send(embed=e)
    em = discord.Embed(title=None, description=msg, timestamp = datetime.datetime.utcnow(), colour=0x6c85ff)
    em.set_author(name=author.display_name, icon_url=author.avatar_url)
    emb = discord.Embed(title='📬 Жалоба отправлена!', description='Ваша жалоба была отправлена администрации сервера.', colour=0x6c85ff)
    await channel.send(embed=em)
    await ctx.send(embed=emb, delete_after=10.0)
    if isinstance(ctx.channel, discord.abc.GuildChannel):
        await ctx.message.delete()
    else:
        pass

@bot.command(aliases = ["creports"])
@commands.has_permissions(administrator=True)
async def createreports(ctx):
    ch = discord.utils.get(bot.get_all_channels(), name='reports')
    guild = ctx.message.guild
    overwrites = {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    guild.me: discord.PermissionOverwrite(read_messages=True)
}
    if ch is None:
        try:
            await guild.create_text_channel('reports', overwrites=overwrites)
        except discord.Forbidden:
            await ctx.send('У меня нет прав на создание этого канала')
        else:
            e = discord.Embed(title='✅ Канал создан!', description='Канал для жалоб был успешно создан.', colour=0x6c85ff)
            await ctx.send(embed=e)
    if ch is not None:
        em = discord.Embed(title=None, description='❌ Канал уже существует.', colour=0x6c85ff)
        await ctx.send(embed=em)

@bot.command()
@commands.is_owner()
async def about(ctx):
    e = discord.Embed(title=None, description='Привет. Я - {}. Бот, созданный специально для сервера **All For You**.'.format(bot.user.name), colour=0x6c85ff)
    e.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    e.set_footer(text='version: 0.0.1 ')
    e.set_thumbnail(url=bot.user.avatar_url)
    await ctx.send(embed=e)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run('MzM2ODg0Nzg5NjE5NzIwMjEz.DFrRsg.m4sjtB6t7savskFTHmcETg5nwFo')