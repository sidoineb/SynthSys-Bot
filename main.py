import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = discord.Client()

@client.event
async def on_message(message):
    print(f'{client.user} est connecté sur le Discord!')

    if message.content.startswith('!bonjour'):
        await message.channel.send('Bonjour {client.user}!')

client.run(TOKEN)