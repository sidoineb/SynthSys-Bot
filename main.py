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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Vous n'avez pas les permissions nécessaires pour exécuter cette commande.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Commande non trouvée.")
    else:
        await ctx.send("Une erreur est survenue lors de l'exécution de la commande.")

# Chargement des cogs
extensions = ['cogs.admin', 'cogs.misc']

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

# Démarrage du bot
bot.run(TOKEN)