import nextcord
from nextcord.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="clear", description="Clear up some messages!")
    async def clear(self, ctx, quantity: int):
        await ctx.channel.purge(limit=quantity)
        await ctx.send(f"Cleared {quantity} messages!", delete_after=3)


def setup(bot):
    bot.add_cog(Clear(bot))