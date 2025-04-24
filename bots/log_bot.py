import discord

intents = discord.Intents.default()
intents.messages = True

bot = discord.Client(intents=intents)

LOG_CHANNEL_ID = 1234567890123456

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # only log if message is not send by bots
    if message.author == bot.user:
        return 

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel and message.channel.id != LOG_CHANNEL_ID:
        await log_channel.send(
            f"**User:** {message.author} | **Channel:** {message.channel.name}\n**Message:** {message.content}"
        )

bot.run("your bot token here!")
