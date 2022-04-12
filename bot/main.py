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
    target1_channel = guild.get_channel(951638778160750603)
    # Fetch target roles
    role_1 = guild.get_role(953020148623749191)
    # role_2 = guild.get_role(953020148623749191)

    if role_1 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_1.id}>")
        embed = discord.Embed(
            title=msg,
            color=0xe0dd12,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value="Futures")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        noti1 = await target1_channel.send(msg + " - " + "<@&953020148623749191>")
        await noti1.delete()
        message = await target1_channel.send(embed=embed)
        await target.add_reaction("👍")
        

    elif role_2 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_2.id}>")
        embed = discord.Embed(title=msg, color=0xe0dd12, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_2.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target1_channel.send(embed=embed)
        await message.channel.send(embed=embed)
        
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
