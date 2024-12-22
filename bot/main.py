import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Intents are required for receiving certain events like messages
intents = discord.Intents.default()
intents.messages = True  # Enable message-related events
intents.message_content = True  # Enable access to message content
# Set up the bot
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")


# Run the bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot.run(BOT_TOKEN)

