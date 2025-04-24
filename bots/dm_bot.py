import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot user: {bot.user}")

# to send a dm to an user
#! WARNING !# BOT CAN ONLY SEND A DM IF THE USER IS IN THE SERVER AND HAS DM's ON!
@bot.command()
async def send_dm(ctx, user: discord.User, *, message: str):
    try:
        await user.send(message)
        await ctx.send(f"Successfully send message to {user.name}!")
    except Exception as e:
        await ctx.send(f"`Error while sending {user.name} the message`. (Console for Errorcode)")
        print(e)

bot.run("your bot token here!")
