from discord.ext import commands
import discord

BOT_TOKEN = ""
CHANNEL_ID = 32

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    # print("H??????")
    channel = bot.get_channel(CHANNEL_ID)
    # await channel.send("i am here G what do you want ong!")


@bot.command()
async def hello(ctx):
    await ctx.send("")


@bot.command()
async def overwatch_shit_talk(ctx):
    await ctx.send("")


@bot.command()
async def are_you_fat(ctx):
    await ctx.send("")

bot.run(BOT_TOKEN)
