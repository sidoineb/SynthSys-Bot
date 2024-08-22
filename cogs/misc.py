import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(
            title=f"Avatar de {member.name}",
            description=f"[Lien vers l'avatar]({member.display_avatar.url})",
            color=discord.Color.green()
        )
        embed.set_image(url=member.display_avatar.url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))
