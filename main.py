import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('Ici mettre le Token')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} est connecté sur le Discord!')

client.run(TOKEN)