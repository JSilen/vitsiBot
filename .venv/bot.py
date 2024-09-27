import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json
import random

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

with open('jokes.json', 'r', encoding='utf-8') as file:
    jokes = json.load(file)["jokes"]

@bot.event
async def on_ready():
    print(f'Olen kirjautunut sisään nimellä {bot.user}')

@bot.command()
async def vitsi(ctx):
    random_joke = random.choice(jokes)["text"]
    await ctx.send(random_joke)

bot.run(TOKEN)