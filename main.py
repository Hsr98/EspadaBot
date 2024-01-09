from discord.ext import commands
import discord

BOT_TOKEN = ""
CHANNEL_ID = ""

bot = commands(command_prefix="!", intents=discord.intent.all())


@bot.event
async def on_ready():
    print("bruh ong ong wth do you want? (i am working, smh)")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello")


@bot.commad()
async def hello(ctx, x, y):
    await ctx.send("hello")


bot.run(BOT_TOKEN)
