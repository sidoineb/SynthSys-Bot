import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = discord.Client()

# Accueil

@client.event
async def on_message(message):
    print(f'{client.user} est connecté sur le Discord!')

    if message.content.startswith('!bonjour'):
        await message.channel.send('Bonjour {client.user}!')


# Kick

@client.command()
async def kick(ctx, user:discord.User, reason):
    if ctx.author.guild_permissions.kick_members:
        await ctx.guild.kick(user)
        await ctx.respond(f'Kick de {user} - Raison: (reason)')

    else:
        await ctx.respond("Vous n'avez pas les droits pour Kick un membre!")

# Ban

@client.command()
async def ban(ctx, user:discord.User, reason):
    if ctx.author.guild_permissions.ban_members:
        await ctx.guild.ban(user)
        await ctx.respond(f'ban de {user} - Raison: (reason)')

    else:
        await ctx.respond("Vous n'avez pas les droits pour Ban un membre!")

# Unban

@client.command()
async def unban(ctx, user:discord.User, reason):
    if ctx.author.guild_permissions.ban_members:
        await ctx.guild.unban(user)
        await ctx.respond(f'Unban de {user} - Raison: (reason)')

    else:
        await ctx.respond("Vous n'avez pas les droits pour Unban un membre!")


client.run(TOKEN)