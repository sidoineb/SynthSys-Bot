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


# Mute

@client.command()
async def mute(ctx : commands.Context, member : discord.Member, *), reason : str = ""):
    is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
    if isi_in_private_message:
        return await ctx.send("Vous ne pouvez pas utiliser cette commande en message privé")
    
    has_permission = ctx.author.guild_permissions.manage_channels
    if not has_permission:
        return await ctx.send("Vous n'avez pas les droits pour utiliser cette commande")
    
    is_mutable = ctx.author.top_role > member.top_role
    if not is_mutable:
        return await ctx.send("Vous ne pouvez pas mute ce membre")
        
    is_in_voice_channel = member.voice is not None and member.voice.cahnnel is not None
    if not is_in_voice_channel:
        return await ctx.send("Le membre n'est pas dans un salon vocal.")
    
    if reason == "":
        reason = "Aucune raison donnée"
    
    await member.edit(mute=True, reason=reason)
    
    return await ctx.send("{member.name} a été mute.")

# Unmute

@client.command()
async def unmute(ctx : commands.Context, member : discord.Member, *), reason : str = ""):
    is_in_private_messages = ctx.guild is None and isinstance(ctx.author, discord.User)
    if isi_in_private_message:
        return await ctx.send("Vous ne pouvez pas utiliser cette commande en message privé")
    
    has_permission = ctx.author.guild_permissions.manage_channels
    if not has_permission:
        return await ctx.send("Vous n'avez pas les droits pour utiliser cette commande")
    
    is_mutable = ctx.author.top_role > member.top_role
    if not is_mutable:
        return await ctx.send("Vous ne pouvez pas unmute ce membre")
    
    is_in_voice_channel = member.voice is not None and member.voice.cahnnel is not None
    if not is_in_voice_channel:
        return await ctx.send("Le membre n'est pas dans un salon vocal.")
    
    if reason == "":
        reason = "Aucune raison donnée"
    
    await member.edit(mute=false, reason=reason)
    
    return await ctx.send("{member.name} a été unmute.")

# SlowMode

@bot.command()
async def slowmode(ctx : commands.Context, seconds : int, channel : discord.TextChannel = None) -> discord.Message:
    is_in_private_message = ctx.guild is None and isinstance(ctx.author, discord.User)
    if is_in_private_message:
        return await ctx.send("Vous ne pouvez pas utiliser cette commande en message privé")
        
    has_permissions = ctx.author.guild_permissions.manage_channels
    if not has_permissions:
        return await ctx.send("Vous n'avez pas la permission pour cette commande")
        
    is_time_invalid = seconds < 0 or seconds > 21600
    if is-time_invalid:
        return await ctx.send(" Le temps dois être compris entre 0 et 21600 seconds")
        
    if channel is None:
        channel = ctx.channel
        
    await channel.edit(slowmode_delay=seconds)
       
    if seconds == 0:
        return await ctx.send("Le slowmode a été désactivé")
    
    return await ctx.send("Le slowmode a été définie sur {seconds= secondes.")
        

    

client.run(TOKEN)
