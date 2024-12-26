import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason is None:
            await ctx.send("Veuillez entrer une raison pour le kick.")
        else:
            await member.kick(reason=reason)
            await ctx.send(f'{member.name} a été kické pour la raison suivante : {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if reason is None:
            await ctx.send("Veuillez entrer une raison pour le ban.")
        else:
            await member.ban(reason=reason)
            await ctx.send(f'{member.name} a été banni pour la raison suivante : {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member_name):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member_name.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} a été débanni.')
                return

        await ctx.send(f'{member_name}#{member_discriminator} n\'a pas été trouvé.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int, channel: discord.TextChannel = None):
        if seconds < 0 or seconds > 21600:
            await ctx.send("Le temps doit être compris entre 0 et 21600 secondes.")
            return

        if channel is None:
            channel = ctx.channel

        await channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Le slowmode a été défini à {seconds} secondes.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")

            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False)

        await member.add_roles(mute_role, reason=reason)
        await ctx.send(f'{member.name} a été mute pour la raison suivante : {reason}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f'{member.name} a été unmute.')
        else:
            await ctx.send(f'{member.name} n\'est pas mute.')

def setup(bot):
    bot.add_cog(Admin(bot))