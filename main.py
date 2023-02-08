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
async def kick(ctx, user: discord.User, reason: str):

    if ctx.author.guild_permissions.kick_members is True:
        if reason:
            await ctx.guild.kick(user, reason=reason)
            await ctx.send(f"Utilisateur kické: {user.name} ({user.id}) - Raison: {reason}")
        else:
            await ctx.send("Veuillez entrer une raison pour le kick.")
        else:
        await ctx.send("Vous n'avez pas la permission de bannir un utilisateur.")


# Ban

@client.command()
async def ban(ctx, user: discord.User, reason: str):

    if ctx.author.guild_permissions.ban_members is True:
        if reason:
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(f"Utilisateur banni: {user.name} ({user.id}) - Raison: {reason}")
        else:
            await ctx.send("Veuillez entrer une raison pour le bannir.")
        else:
        await ctx.send("Vous n'avez pas la permission de bannir un utilisateur.")


# Unban

@client.command()
async def unban(ctx, user: discord.User, reason: str):

    if ctx.author.guild_permissions.ban_members is True:
        if reason:
            await ctx.guild.unban(user, reason=reason)
            await ctx.send(f"Utilisateur unbanni: {user.name} ({user.id}) - Raison: {reason}")
        else:
            await ctx.send("Veuillez entrer une raison pour le unbannir.")
        else:
        await ctx.send("Vous n'avez pas la permission de unbannir un utilisateur.")

client.run(TOKEN)