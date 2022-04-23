import os
import discord
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents = intents)
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.listen()
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    # Fetch target channels
    futures_channel = guild.get_channel(951638778160750603)
    options_channel = guild.get_channel(967359150176747621)
    commentary_channel = guild.get_channel(967358615017115658)
    # Fetch target roles
    futures_role = guild.get_role(953020148623749191)
    options_role = guild.get_role(967361125068972043)
    commentary_role = guild.get_role(967368279595315200)

    if futures_role in message.role_mentions:
        msg = message.content.strip(f"<@&{futures_role.id}>")
        embed = discord.Embed(
            title=msg,
            color=0xe0dd12,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value="Futures")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await futures_channel.send(msg + " - " + f"<@&{futures_role.id}>")
        await noti.delete()
        message = await futures_channel.send(embed=embed)
        await message.add_reaction("👍")
        

    elif options_role in message.role_mentions:
        msg = message.content.strip(f"<@&{options_role.id}>")
        embed = discord.Embed(title=msg, color=0x9b59b6, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value="Options Play")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await options_channel.send(msg + " - " + f"<@&{options_role.id}>")
        await noti.delete()
        message = await options_channel.send(embed=embed)
        await message.add_reaction("👍")
        
    elif commentary_role in message.role_mentions:
        msg = message.content.strip(f"<@&{commentary_role.id}>")
        embed = discord.Embed(
            title="** **",
            description=msg,
            color=0x187bcd,
            timestamp=datetime.now(),
        )
        # embed.add_field(name="Trade Type:", value="Options Play")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await commentary_channel.send(msg + " - " + f"<@&{commentary_role.id}>")
        await noti.delete()
        message = await commentary_channel.send(embed=embed)
        await message.add_reaction("👍")
        
@bot.listen()
async def on_message(message):
  '''simple on message to respond if a message containing "hello" is sent'''
  # prevent bot from answering other bots, including self
  if message.author.bot:
     return
  # create message content and channel variables
  content = message.content.lower()
  channel = message.channel
  # check if message includes "hello"
  if 'did we do today' in content:
    msg = await channel.send('yeah, you bank on these dank callouts or fuck it up?')
    await msg.add_reaction("🟢")
    await msg.add_reaction("🔴")

        
@bot.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    bot.run(TOKEN)
