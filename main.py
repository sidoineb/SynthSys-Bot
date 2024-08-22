import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Chargement du token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Permissions
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

# Initialisation
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} est connecté !')

# Chargement des cogs
extensions = ['cogs.admin', 'cogs.misc']

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

# Démarrage du bot
bot.run(TOKEN)